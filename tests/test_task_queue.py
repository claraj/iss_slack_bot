import sys
sys.path.insert(1, '/Users/admin/gcloud/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, '/Users/admin/gcloud/google-cloud-sdk/platform/google_appengine/lib/yaml/lib')

import logging
logging.getLogger().setLevel(logging.DEBUG)

from unittest import TestCase
from google.appengine.api import taskqueue
from google.appengine.ext import testbed

from datetime import datetime, timedelta
import time
import calendar

import mock
from mock import MagicMock

import passtimes_worker
from passtimes_worker import NoFutureTimesFoundException
import iss_api

from pytz import timezone

## Tests for functions that work with the tasks queue
## Verify correct behavior when these are called

class TestPassTimesWorkerQueueCall(TestCase):
    # mock slack API endpoint, verify correct call is made

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_taskqueue_stub(root_path='.')
        self.taskqueue_stub = self.testbed.get_stub(testbed.TASKQUEUE_SERVICE_NAME)

    def tearDown(self):
        self.testbed.deactivate()


    def utc_ts(self, dt):
        ''' return a timestamp for a datetime IN UTC '''
        # print(dt, dt.utctimetuple())
        timestamp = calendar.timegm(dt.utctimetuple())
        # print(timestamp)
        return timestamp


    def testEnqueueNextPassTimeOnePastSomeFutureTimes(self):

        ''' Should add the pass time that's one hour in the future to the queues '''

        # Mock iss.get_next_pass to return spcific values

        utc = timezone('UTC')
        ct = timezone('US/Central')

        # Times in UTC
        utc_now = datetime.now(utc)
        utc_five_minutes_in_future = utc_now + timedelta(minutes=5)
        utc_eighty_minutes_in_future = utc_now + timedelta(minutes=80)

        expected_new_task_ts = self.utc_ts(utc_eighty_minutes_in_future)
        print('expect new task ts = ', expected_new_task_ts)

        # Time now, and accceptable time 80 mins in the future
        mock_pass_times = [ { 'risetime' : self.utc_ts(utc_now) , 'duration': 3 },
            { 'risetime' : self.utc_ts(utc_five_minutes_in_future), 'duration' : 6 },
            { 'risetime' : self.utc_ts(utc_eighty_minutes_in_future), 'duration' : 6 }
        ]

        iss_api.get_next_pass = MagicMock(return_value = mock_pass_times )

        passtimes_worker.request_and_enqueue_next_pass()

        ## Check Slack post tasks queue

        # The utc_eighty_minutes_in_future time should be enqueued
        slack_tasks = self.taskqueue_stub.get_filtered_tasks(queue_names='slack')
        self.assertEqual(1, len(slack_tasks))

        first_slack_task = slack_tasks[0]

        iss_slack_task_eta_ts = self.utc_ts(first_slack_task.eta)
        utc_eighty_minutes_in_future_ts = self.utc_ts(utc_eighty_minutes_in_future)

        self.assertEqual(utc_eighty_minutes_in_future_ts, iss_slack_task_eta_ts)
        self.assertEqual('/post_to_slack', first_slack_task.url )
        self.assertEqual('iss_at_' + str(utc_eighty_minutes_in_future_ts), first_slack_task.name)


        ## Check get next pass time queue
        get_next_pass_tasks = self.taskqueue_stub.get_filtered_tasks(queue_names='passtimes')
        self.assertEqual(1, len(get_next_pass_tasks))
        self.assertEqual(self.utc_ts(utc_eighty_minutes_in_future), self.utc_ts(get_next_pass_tasks[0].eta))
        self.assertEqual('get_next_pass_' + str(utc_eighty_minutes_in_future_ts), get_next_pass_tasks[0].name)
        self.assertEqual('/enqueue_next_pass_time', get_next_pass_tasks[0].url)



    def testEnqueueNextPassTimeNoFutureTimes(self):

        ''' Should throw a NoFutureTimesFoundException
        '''

        # Mock iss.get_next_pass to return spcific values

        # Only times are in the past
        mock_pass_times = [ { 'risetime' : 20 , 'duration': 3 } ]

        iss_api.get_next_pass = MagicMock(return_value = mock_pass_times )

        with self.assertRaises(NoFutureTimesFoundException):
            passtimes_worker.request_and_enqueue_next_pass()



    def testEnqueueNextPassNoTimes(self):

        ''' Should throw a NoFutureTimesFoundException
        '''

        # Mock iss.get_next_pass to return specific values

        # No times
        mock_pass_times = [ ]

        iss_api.get_next_pass = MagicMock(return_value = mock_pass_times )

        with self.assertRaises(NoFutureTimesFoundException):
            passtimes_worker.request_and_enqueue_next_pass()



    def testEnqueueNextPassErrorInFetch(self):

        ''' Should throw a NoFutureTimesFoundException
        '''

        # Mock iss.get_next_pass to return specific values

        # No
        mock_pass_times = None

        iss_api.get_next_pass = MagicMock(return_value = mock_pass_times )

        with self.assertRaises(NoFutureTimesFoundException):
            passtimes_worker.request_and_enqueue_next_pass()
