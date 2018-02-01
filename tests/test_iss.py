from unittest import TestCase

from datetime import datetime, timedelta
import time
import config
import iss_api
import logging
from logging import Logger

logging.getLogger().setLevel(logging.DEBUG)
# Connect to mock ISS API and verify expected results are returned
# Works with iss_api.py

class TestMockISSAPICall(TestCase):


    mock_api_url = 'http://127.0.0.1:3000/iss-pass.json'

    def setUp(self):
        config.iss_api_endpoint_url = self.mock_api_url


    # mock iss api, verify calling
    def test_fetch_iss_results(self):

        print(config.iss_api_endpoint_url)
        expected = [
            {"risetime": 4000, "duration": 5},
            {"risetime": 6050, "duration": 12},
            {"risetime": 12000, "duration": 4}
          ]

        res = iss_api.get_next_pass(1, 2, 3)
        print(res)
        self.assertEqual(expected, res)



    def fetch_with_errors(self):
        self.fail('implement me ')
