#!/usr/bin bash
import urllib.request
url = "https://alx-intranet.hbtn.io/status"

try: 
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
except Exception as e:
    print("Error: {}".format(e))