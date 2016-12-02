import json
import urllib.request

BASE_URL = "https://earthview.withgoogle.com/"
START_JSON = "/_api/kane-county-united-states-1256.json"

ret = urllib.request.urlopen(BASE_URL + START_JSON).read()
js = json.loads(ret)