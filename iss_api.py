import urllib
import urllib2
import logging
import json
import config

def get_next_pass(lat, lon, passes):

    location = {'lat': lat, 'lon': lon, 'n': passes}
    data = urllib.urlencode(location)

    url = config.iss_api_endpoint_url

    full_url = url + '?' + data

    logging.debug('about to request: ' + full_url)

    try:
        response = urllib2.urlopen(full_url)
        txt = response.read().decode('utf-8')
        res_json = json.loads(txt)
        logging.debug('data received was: ' + json.dumps(res_json))
        return res_json['response']

    except Exception as e:
        logging.error('Error connecting to Open-Notify ISS API because ' + str(e))



if __name__ == '__main__':
    # Used for testing this module at the command line
    passes = get_next_pass(45, -93, 2)
    print(passes)
