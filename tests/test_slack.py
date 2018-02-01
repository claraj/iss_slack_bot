from unittest import TestCase

from datetime import datetime, timedelta
import time

import slack_post

# Make call to mock Slack endpoint and verify correct HTTP call is made
# Works with slack_post

class TestMockSlackPost(TestCase):
    # mock iss api, verify calling
    def test_slack_post(self):
        self.fail('implement me')
