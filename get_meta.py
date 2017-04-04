#!/usr/bin/env python3

import urllib.request
import urllib.parse

import itertools
import json
import sys
import os

def uprint(s):
    sys.stdout.buffer.write(s.encode(sys.stdout.encoding, errors='replace'))
    print('')

BASE_URL = 'https://earthview.withgoogle.com/'
START_JSON = '/_api/kane-county-united-states-1256.json'
JSON_DIR = 'json'

# Setup folders
if not os.path.isdir(JSON_DIR):
    if os.path.exists(JSON_DIR):
        os.remove(JSON_DIR)
    os.makedirs(JSON_DIR)

f = open('out.txt', 'wb')

cur_json_url = START_JSON
for i in itertools.count():
    # Download JSON
    url = BASE_URL + urllib.parse.quote(cur_json_url, encoding='utf-8')
    ret = urllib.request.urlopen(url).read()
    rets = ret.decode('utf-8')
    
    # Decode JSON
    js = json.loads(rets)
    
    # Write JSON URL to output file
    f.write(cur_json_url.encode('utf-8'))
    f.write('\r\n'.encode('utf-8'))
    f.flush()
    
    # Write JSON to json/<id>
    json_id = int(js['id'])
    json_file = open('{}/{:04}.json'.format(JSON_DIR, json_id), 'wb')
    json_file.write(json.dumps(js))
    json_file.flush()
    json_file.close()
    
    # Print out and set new JSON URL
    uprint('{:04} ({:04}): "{}": {}'.format(i, json_id, js['title'], js['photoUrl']))
    cur_json_url = js['nextApi']
    if cur_json_url == START_JSON:
        print('Back to beginning.. Exiting.')
        break;

f.close()
