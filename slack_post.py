import urllib
import urllib2

import logging
import json
import os

from datetime import datetime, tzinfo

import secrets


def message_slack(msg):
    '''
    curl -X POST
      -H 'Content-type: application/json'
        --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/NUMBERS/MORENUMBERS/ETC
    '''

    webhook_url = secrets.SLACK_ISS_WEBHOOK_URL

    post_data = { "text": msg }

    # Turn JSON to a string and encode as utf-8
    data = json.dumps(post_data).encode('utf-8')

    # dictionary of headers, indicating data is JSON
    headers = {"Content-Type": "application/json"}

    try:
        request = urllib2.Request(webhook_url, data, headers)
        response = urllib2.urlopen(request).read()
        logging.info('Messaged slack with the following message: ' + msg + ' and recieved this response: ' + response)

    except urllib2.URLError as e:
        logging.error('Failed to post message to slack because of ' + e.reason)



if __name__ == '__main__':
    # Used for testing locally
    message_slack('hello, this is a test.')
