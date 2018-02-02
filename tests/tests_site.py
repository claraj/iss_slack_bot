from unittest import TestCase

from datetime import datetime, timedelta
import time


class TestSitePages(TestCase):

    def test_open_home_page(self):
        self.fail('implement me')  # 200 and message

    def test_404_message(self):
        self.fail('implement me')  # Everything else should show custom 404 message

    def test_no_access_to_admin_routes(self):
        self.fail('implement me')


    def testSlackPostInvoked(self):
        fail('implement me')
        ## mock the slack post method and check it was called
        # when /post_to_slack is requested
