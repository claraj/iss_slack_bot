from google.appengine.api import taskqueue
from google.appengine.api.taskqueue import DuplicateTaskNameError, TombstonedTaskError, TaskAlreadyExistsError

import logging
from datetime import datetime

import iss_api as iss
import config
from utils import in_future


import app_factory

app = app_factory.factory()


class NoFutureTimesFoundException(Exception):
    pass


@app.route('/enqueue_next_pass_time', methods=['POST'])
def get_next_pass_info_and_enqueue():
    success = request_and_enqueue_next_pass()
    if success:
        return success
    else:
        abort(500)


def request_and_enqueue_next_pass():
    '''
    Make request, get next pass time
    enqueue task slack task at that pass time
    enqueue get next task task at that pass time
    '''

    logging.info('Requesting set of next pass times')

    next_passes = iss.get_next_pass(config.lat, config.lon, 3) or []   # Returns None in event of error, replace with []

    # If the ISS is above right now, the first time returned by the ISS API may be
    # the current time. This should be ignored as have just posted this.
    next_future_pass = [ p for p in next_passes if in_future(p['risetime'], config.min_time_in_future) ]

    if next_future_pass:
        next_time = next_passes[0]['risetime']
        seconds = next_passes[0]['duration']
        eta = datetime.fromtimestamp(next_time)

        message = config.slack_message_text % seconds
        logging.info('Enqueuing new pass time at %f, of %s seconds, with ETA of %s' % (next_time, seconds, eta) )

        name = 'iss_at_%.0f' % next_time

        try:
            task = taskqueue.add(
                queue_name = 'slack',
                name = name,              # prevent duplicates
                url = '/post_to_slack',
                target = 'iss_worker',
                eta = eta,
                params = {'message': message, 'risetime': next_time}
            )

        except (DuplicateTaskNameError, TaskAlreadyExistsError, TombstonedTaskError) as e:
            logging.warning('Task with name ' + name + ' already exists (or has existed) in slack notification queue. ' + str(e))


        # And add a task to do this again, at the same time as the slack post task
        task = taskqueue.add(
            queue_name = 'passtimes',
            url = '/enqueue_next_pass_time',
            target = 'passtimes_worker',
            eta = eta
        )

        logging.info('Next pass enqueued')
        return 'Next pass time ' + str(eta) + ' enqueued'


    else:
        # Cause task to fail. The queue will retry after the min-retry-time specified in queue.yaml
        raise NoFutureTimesFoundException()
