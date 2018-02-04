import slack_post
import logging
import app_factory
from flask import request

app = app_factory.factory()


# Invoked when the ISS is above. Posts to Slack.

@app.route('/post_to_slack', methods=['POST'])
def iss_is_above_right_now():

    message = request.form.get('message')
    message = message if message else 'The ISS is above!'

    logging.debug('iss is above right now, posting message to slack ' + message)

    slack_post.message_slack(message)

    return 'ok'
