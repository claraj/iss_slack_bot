import slack_post
import logging
import app_factory


app = app_factory.factory()


# Invoked when the ISS is above. Posts to Slack and
# starts a new request to find the next time.

@app.route('/iss_is_above_right_now', methods=['POST'])
def iss_is_above_right_now():

    message = request.form.get('message')
    message = message if message else 'The ISS is above!'

    logging.debug('iss is above right now, posting message to slack ' + message)

    slack_post.message_slack(message)

    return 'ok'
