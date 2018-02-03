## Slack ISS flyover notification bot

### Run dev server

```
dev_appserver.py app.yaml
```

App will be at 127.0.0.1:8080
App admin console at 127.0.0.1:8000

### Starting app

Visit any URL for your app

You may need to purge your task queue in the console when re-starting.


### Secrets

Requires a Slack webhook URL. Provide a file secrets.py with the line

```
SLACK_ISS_WEBHOOK_URL = 'https://webhooks.slack.com/whatever/your/url/is'
```

### Tests


Run all the tests
```
python -m unittest discover tests  
```
Run one test (example)

```
python -m unittest tests.test_utils
```

Slack test and ISS tests require a mock API running locally. See https://github.com/minneapolis-edu/mock_iss_api
https://github.com/minneapolis-edu/mock_slack_api


### TODO

Finish tests

Better way to start application.
Verify post routes are not answering to any outside calls
Redirect all routes to home page

Flush queues on app re-deploy?


Tests ...
add location of libraries to path
https://stackoverflow.com/questions/36073263/importerror-cannot-import-name-wraps-on-mac

six issues, with mock https://stackoverflow.com/questions/36073263/importerror-cannot-import-name-wraps-on-mac
