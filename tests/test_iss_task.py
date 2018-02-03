from unittest import TestCase

from datetime import datetime, timedelta
import time
import config
import iss_api
import logging
from logging import Logger

logging.getLogger().setLevel(logging.DEBUG)




class Iss_Is_Above_Ensure_Slack_Post_Invoked(TestCase):


    def testIssIsAboveNow(self):
        self.fail('implement me')
        # Move to new test class ?
