from unittest import TestCase
from google.appengine.ext import testbed
from google.appengine.api import TaskQueue

from datetime import datetime, timedelta
import time


## Tests for functions that work with the tasks queue
## Verify correct behavior when these are called

class TestPassTimesWorkerQueueCall(TestCase):
    # mock slack API endpoint, verify correct call is made

    def setUp():
        self.testbed = testbed.TestBed()
        self.testbed.activate()
        self.testbed.init_taskqueue_stub()

    def tearDown(self):
        self.testbed.deactivate()


    def testEnqueueNextPassTime(self):


        fail('implement me')



    def testIssIsAboveNow(self):
        fail('implement me')
