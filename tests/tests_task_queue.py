from unittest import TestCase
from google.appengine.ext import testbed
from google.appengine.api import TaskQueue

from datetime import datetime, timedelta
import time


## Tests for functions that work with the tasks queue
## Verify correct behavior when these are called 

class TestMockSlackPostCall(TestCase):
    # mock slack API endpoint, verify correct call is made

    def setUp():
        self.testbed = testbed.TestBed()
        self.testbed.activate()
        self.testbed.init_taskqueue_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_post_to_slack(self):
        self.fail('implement me')



class TestMockISSFetchAPICall(TestCase):
    # mock iss api, verify calling
    def test_fetch_iss_results(self):
        self.fail('implement me')



class TestEnqueueNextPassTime(TestCase):
    def test_enqueue_next_pass(self):
        self.fail('implement me')
