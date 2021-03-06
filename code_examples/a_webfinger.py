#!/usr/bin/env python
"""
Code to show how you can use WebFinger to acquire the issuer ID
of an OpenID Connect provider using an account id
"""

import json
import requests

from oic.oauth2 import PBase
from oic.utils.webfinger import OIC_ISSUER
from oic.utils.webfinger import WebFinger

from requests.packages import urllib3
urllib3.disable_warnings()

__author__ = 'roland'

# =====================================================================
# Using only very basic functions and methods

# Initiate the WebFinger class
wf = WebFinger()

RESOURCE = "acct:carol@op1.test.inacademia.org"
# contruct the webfinger query URL
query = wf.query(RESOURCE, rel=OIC_ISSUER)

print(60*'-')
print('QUERY:{}'.format(query))
print(60*'-')

r = requests.request("GET", query, verify=False)

# parse the JSON returned by the website and dump the content to
# standard out
jwt = json.loads(r.text)
print(json.dumps(jwt, sort_keys=True, indent=4, separators=(',', ': ')))

# =====================================================================
# A bit more high level
print(60*'=')

wf = WebFinger()

# PBase is a wrapper around requests
wf.httpd = PBase(verify_ssl=False)

# discover_query will follow webfinger redirects
url = wf.discovery_query(RESOURCE)
print(url)