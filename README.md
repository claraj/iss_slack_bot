## Slack ISS flyover notification bot

### Run dev server

```
dev_appserver.py app.yaml
```

App will be at 127.0.0.1:8080


### Starting app

Visit any URL for your app


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
python -m unittest tests.tests_utils
```

### TODO

Mock ISS API for testing
Mock Slack API for testing
Better way to start application.
Verify post routes are not answering to any outside calls
