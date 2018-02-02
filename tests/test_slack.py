from unittest import TestCase

import logging

import config
import slack_post

# logging.getLogger().setLevel(logging.DEBUG)

# Make call to mock Slack endpoint and verify correct HTTP call is made
# Works with slack_post

class TestMockSlackPost(TestCase):
    # mock iss api, verify calling

    def setUp(self):

        config.SLACK_ISS_WEBHOOK_URL = 'http://127.0.0.1:3000/fake_slack/'

    def test_slack_post(self):

        response, status_code = slack_post.message_slack('Testing!')
        assert 200 <= status_code <= 299
