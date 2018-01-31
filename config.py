# How far in the future a pass time has to be, to considered to be a new pass
min_time_in_future = 60 * 10

# Lat and lon of Minneapolis
lat = 45
lon = -93

location = 'Minneapolis'

# Message text to post to Slack
slack_message_text = 'Look up! The ISS will be above ' + location + ' for %d seconds!'


# If ISS API returns no results, wait this many minutes before trying again
iss_api_retry_delay_minutes = 60
