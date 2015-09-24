#!/usr/bin/env python

import json
import requests
from oic.oauth2 import PBase
from oic.oic import OIDCONF_PATTERN
from oic.utils.webfinger import WebFinger

# This is a complete discovery example with OpenID Connect. After having retrieved the provide URL, its information
# is retrieved and printed. The standard URL format for obtaining OP information is:
# https://<op.servername>/.well-known/openid-configuration

userid = "carol@oictest.umdc.umu.se:8060"
wf = WebFinger()
wf.httpd = PBase(verify_ssl=False)
url = wf.discovery_query("acct:%s" % userid)

print "Provider:", url

if url[-1] == '/': url = url[:-1]
url = OIDCONF_PATTERN % url

print "Provider info url:", url

r = requests.request("GET", url, verify=False)

jwt = json.loads(r.text)
print "---- provider configuration info ----"
print json.dumps(jwt, sort_keys=True, indent=4, separators=(',', ': '))