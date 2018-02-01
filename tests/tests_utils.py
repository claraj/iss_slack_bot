from unittest import TestCase
from utils import in_future

from datetime import datetime, timedelta
import time

# Testing functions unrelated to GAE features

class TestInFuture(TestCase):

    def setUp(self):
        self.now = datetime.today()
        self.add_ten_seconds = timedelta(seconds = 10)
        self.add_fourty_seconds = timedelta(seconds = 40)
        # self.subtract_ten_seconds = timedelta(seconds = -10)
        # self.subtract_fourty_seconds = timedelta(seconds = -40)


    def test_in_future(self):

        # Example: pass_time is 10 seconds in the future. Return True
        now_plus_ten = self.now + self.add_ten_seconds
        now_plus_ten_ts = time.mktime(now_plus_ten.timetuple())          # Python 3 has a datetime.timestamp() function, but...
        self.assertTrue(in_future(now_plus_ten_ts))


    def test_in_future_now(self):

        # Example: pass_time is now. Return False
        now_ts = time.mktime(self.now.timetuple())
        self.assertFalse(in_future(now_ts))


    def test_in_future_beyond_min(self):

        # Example: pass_time is 10 seconds in the future. min_time_in_future is 5. Return True
        now_plus_ten = self.now + self.add_ten_seconds
        now_plus_ten_ts = time.mktime(now_plus_ten.timetuple())
        self.assertTrue(in_future(now_plus_ten_ts, 5))


    def test_in_future_at_min(self):

        # Example: pass_time is 10 seconds in the future. min_time_in_future is 10. Return False
        now_plus_ten = self.now + self.add_ten_seconds
        now_plus_ten_ts = time.mktime(now_plus_ten.timetuple())
        self.assertFalse(in_future(now_plus_ten_ts, 10))


    def test_in_future_in_past(self):

        # Example: pass_time is in the past. return False
        now_minus_ten = self.now - self.add_ten_seconds
        now_minus_ten_ts = time.mktime(now_minus_ten.timetuple())
        self.assertFalse(in_future(now_minus_ten_ts))


    def test_in_future_in_past_negative_min(self):

        # Example: pass_time is 40 seconds in the past, min_time_delta is -60. return True
        now_minus_fourty = self.now - self.add_fourty_seconds
        now_minus_fourty_ts = time.mktime(now_minus_fourty.timetuple())
        self.assertTrue(in_future(now_minus_fourty_ts, -60))


    def test_in_future_in_past_beyond_negative_min(self):

        # Example: pass_time is 40 seconds in the past, min_time_delta is -10. return False
        now_minus_fourty = self.now - self.add_fourty_seconds
        now_minus_fourty_ts = time.mktime(now_minus_fourty.timetuple())
        self.assertFalse(in_future(now_minus_fourty_ts, -10))
