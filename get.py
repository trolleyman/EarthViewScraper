import json
import urllib.request
import urllib.parse
import sys

def uprint(s):
    sys.stdout.buffer.write(s.encode(sys.stdout.encoding, errors='replace'))
    print('')

BASE_URL = "https://earthview.withgoogle.com/"
START_JSON = "/_api/kane-county-united-states-1256.json"

cur_json_url = START_JSON
i = -1
while True:
    i += 1
    url = BASE_URL + urllib.parse.quote(cur_json_url, encoding='utf-8')
    ret = urllib.request.urlopen(url).read()
    rets = ret.decode('utf-8')
    js = json.loads(rets)
    uprint('{:03}: "{}": {}'.format(i, js['title'], js['photoUrl']))
    cur_json_url = js['nextApi']
    if cur_json_url == START_JSON:
        print('Back to beginning.. Exiting.')
        break;
