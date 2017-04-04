#!/usr/bin/env python3

'''
Gets all of the photos referenced in the json directory
'''

import urllib.request

import os
import json
import sys

def uprint(s):
    sys.stdout.buffer.write(s.encode(sys.stdout.encoding, errors='replace'))
    print('')

JSON_DIR = 'json'
PHOTO_DIR = 'photos'

# Setup folders
if not os.path.isdir(PHOTO_DIR):
    if os.path.exists(PHOTO_DIR):
        os.remove(PHOTO_DIR)
    os.makedirs(PHOTO_DIR)

photo_urls = []
i = 0

for path in os.listdir(JSON_DIR):
    if not path.endswith('.json'):
        continue
    
    # Load JSON file
    file = open('{}/{}'.format(JSON_DIR, path), 'rb')
    json_data = file.read()
    file.close()
    json_str = json_data.decode('utf-8')
    js = json.loads(json_str)
    
    # Download JPG
    photo_data = urllib.request.urlopen(js['photoUrl']).read()
    
    # Calculate title
    striplen = len(' – Earth View from Google');
    title = js['title'][0:-striplen]
    
    # Save to file in photo/<id>
    photo_id = int(js['id'])
    filename = '{:04} - {} ({}, {}).jpg'.format(photo_id, title, js['lat'], js['lng'])
    path_out = '{}/{}'.format(PHOTO_DIR, filename)
    uprint('{:04}: {}'.format(i, filename))
    i += 1
    out = open(path_out, 'wb')
    out.write(photo_data)
    out.close()
