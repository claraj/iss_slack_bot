from flask import Flask, request

from google.appengine.api import taskqueue

import iss_api as iss
import slack_post
from utils import in_future
import config

from datetime import datetime, timedelta
import time
import logging

import app_factory

app = app_factory.factory()


@app.route('/enqueue_next_pass_time', methods=['POST'])
def get_next_pass_info_and_enqueue():
    return request_and_enqueue_next_pass()


@app.route('/post_to_slack', methods=['POST'])
def post_to_slack():

    logging.debug('Posting a message to slack')

    message = request.form.get('message')
    message = message if message else 'The ISS is above!'

    slack_post.message_slack(message)

    return 'ok'


# Invoked when the ISS is above. Posts to Slack and
# starts a new request to find the next time.

@app.route('/iss_is_above_right_now', methods=['POST'])
def iss_is_above_right_now():

    message = request.form.get('message')
    message = message if message else 'The ISS is above!'

    logging.debug('iss is above right now, enqueue slack task to post message ' + message)

    slack_task = taskqueue.add(
        url='/post_to_slack',
        target='iss_worker',
        params={ 'message': message }
    )

    logging.debug('iss is above right now. enqueue task to fetch next time')

    next_pass_task = taskqueue.add(
        url='/enqueue_next_pass_time',
        target='iss_worker',
        params={'last_message_time' : time.time() }
    )

    return 'ok'



def request_and_enqueue_next_pass():
    '''

    Make request, get next pass time
    enqueue task at that pass time
    - this task, when run 1. posts to slack 2. sets up next task
    '''

    logging.info('about to request set of next pass times')
    next_passes = iss.get_next_pass(45, -93, 3)

    # If the ISS is above right now, the first time returned by the ISS API may be
    # the current time. This should be ignored as have just posted this.

    next_future_pass = [ p for p in next_passes if in_future(p['risetime'], config.min_time_in_future) ]


    if next_future_pass:

        next_time = next_passes[0]['risetime']
        seconds = next_passes[0]['duration']
        eta = datetime.fromtimestamp(next_time)

        message = config.slack_message_text % seconds

        task_name = 'iss_post_' + str(next_time)

        logging.info('About to enqueue new pass time at %f, of %s seconds, with ETA of %s' % (next_time, seconds, eta) )

        # try:
        task = taskqueue.add(
            url = '/iss_is_above_right_now',
            # name = task_name,   # Unique name prevents re-adding of same task
            target = 'iss_worker',
            eta = eta,
            params = {'message': message, 'risetime': next_time}
        )

        logging.info('Next pass time identified and enqueued')

        return 'Next pass time ' + str(eta) + ' enqueued'

        # except Exception as e:
        #     logging.error('Error adding next ISS-Is-Above task because ' + str(e))

    if not next_future_pass:
        logging.warning('No future pass times found')

    # Enqueue a task to check again in an hour
    delay = config.iss_api_retry_delay_minutes

    delay_msg = 'Can\'t find or enqueue next ISS pass time. Will try again in %d minutes' % delay
    logging.info(delay_msg)

    task = taskqueue.add(
        url = '/enqueue_next_pass_time',
        target = 'iss_worker',
        eta = datetime.today() + timedelta(minutes=delay)
    )

    return delay_msg
