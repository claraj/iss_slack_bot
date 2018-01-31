import urllib
import urllib2
import logging
import json

def get_next_pass(lat, lon, passes):

    location = {'lat': lat, 'lon': lon, 'n' : passes}
    data = urllib.urlencode(location)

    url = 'http://api.open-notify.org/iss-pass.json'

    full_url = url + '?' + data

    logging.debug('about to request: ' + full_url)

    try:
        response = urllib2.urlopen(full_url)
        txt = response.read().decode('utf-8')
        res_json = json.loads(txt)
        logging.debug('data received was: ' + json.dumps(res_json))
        return res_json['response']

    except Exception as e:
        logging.error('Error connecting to open-notify because ' + str(e))



if __name__ == '__main__':
    passes = get_next_pass(45, -93, 2)
    print(passes)
