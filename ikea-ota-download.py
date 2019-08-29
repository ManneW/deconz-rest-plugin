#!/usr/bin/env python
"""
Snipped to dowload current IKEA ZLL OTA files into ~/otau
compatible with python 3.
"""

import os
import json
import urllib
import urllib.request

f = urllib.request.urlopen("http://fw.ota.homesmart.ikea.net/feed/version_info.json")
data = f.read()

arr = json.loads(data)

otapath = '%s/otau' % os.path.expanduser('~')

if not os.path.exists(otapath):
	os.makedirs(otapath)

for i in arr:
	if 'fw_binary_url' in i:
		url = i['fw_binary_url']
		ls = url.split('/')
		fname = ls[len(ls) - 1]
		path = '%s/%s' % (otapath, fname)

		if not os.path.isfile(path):
			urllib.request.urlretrieve(url, path)
			print(path)
		else:
		    print('%s already exists' % fname)




