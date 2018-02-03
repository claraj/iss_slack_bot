import secrets

# Delay before retry if ISS API is down, or other error fetching data
# If ISS API returns no results, wait this many minutes before trying again
iss_api_retry_delay_minutes = 60


## ISS

# How far in the future a pass time has to be, to considered to be a new pass
min_seconds_in_future = 60 * 10

# Lat and lon of Minneapolis
lat = 45
lon = -93
location = 'Minneapolis'

iss_api_endpoint_url = 'http://api.open-notify.org/iss-pass.json'


## Slack

SLACK_ISS_WEBHOOK_URL = secrets.SLACK_ISS_WEBHOOK_URL


# Message text to post to Slack
slack_message_text = 'Look up! The ISS will be above ' + location + ' for %d seconds!'
