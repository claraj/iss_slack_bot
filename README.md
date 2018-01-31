
## Slack ISS flyover notification bot

### Run dev server

```
dev_appserver.py app.yaml
```

App will be at 127.0.0.1:8080


### Secrets

Requires a Slack webhook URL. Provide a file secrets.py with the line

```
SLACK_ISS_WEBHOOK_URL = 'https://webhooks.slack.com/whatever/your/url/is'
```

### Tests

python -m unittest tests

### TODO

Mock ISS API for testing
Better way to start application.
