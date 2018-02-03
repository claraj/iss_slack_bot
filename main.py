import passtimes_worker
import logging

import app_factory

app = app_factory.factory() #Flask(__name__)


logging.info('Calling initial request for fetch and enqueue next pass')
passtimes_worker.request_and_enqueue_next_pass()

# TODO purge tasks queues on app load? 

@app.route('/')
def example():
    return 'Hello, this is the ISS Slack bot on Google Cloud Platform App Engine.'


# for local development
# or dev_appserver.py app.yaml
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
