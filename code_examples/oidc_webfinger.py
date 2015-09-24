#!/usr/bin/env python

import json
import requests
from oic.oauth2 import PBase
from oic.utils.webfinger import WebFinger, OIC_ISSUER

# In OpenID Connect the first phase for a client authenticating a user requires the client to discover the
# authenticating server. To find the provider it is quite common to use webfinger (RFC 7033).
# When user wants to access a service, he provides a name with a domain (like for instance carol@example.com).
# From the domain, we retrieve an host name that can be used to build a webfinger URI to GET (on https):
#
#      GET /.well-known/webfinger?
#          resource=acct:carol@example.com&&
#          rel=http://openid.net/specs/connect/1.0/issuer
#      HTTP/1.1
#      Host: example.com
#
# This GET will be answered with the required information (the endpoint of the OP):
#
#      HTTP/1.1 200 OK
#      Access-Control-Allow-Origin *
#      Content-Type: application/jrd+json
#
#      {
#           "subject" : "acct:carol@example.com",
#           "links":
#           [{
#               "rel": "http://openid.net/specs/connect/1.0/issuer",
#               "href": "https://openid.example.com"
#           }]
#      }

userid = "carol@op1.test.inacademia.org"

wf = WebFinger()
query = wf.query("acct:%s" % userid, rel=OIC_ISSUER)
print query

r = requests.request("GET", query, verify=False)
jwt = json.loads(r.text)
print json.dumps(jwt, sort_keys=True, indent=4, separators=(',', ': '))
print

#########################################################

wf = WebFinger()
wf.httpd = PBase(verify_ssl=False)
url = wf.discovery_query("acct:%s" % userid)
print "The user should be redirected here for login", url