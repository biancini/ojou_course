#!/usr/bin/env python

from jwkest import b64e
import json

# A specific JWT is a sequence of URL-safe parts separated by a period '.' character.
# All JWT parts are always base64 encoded. A JWT can have different claims (similar to attributes in LDAP world):
# - iss (Issuer) who issued the token
# - sub (Subject) who is described by the token
# - aud (Audience) who the token intended for
# - exp (Expiration Time)
# - nbf (Not Before)
# - iat (Issued At)
# - jti (JWT Id)
#
# An unsecured JWT is the simplest JWT possible. It can be created as follow:
# - create a JOSE header (the simplest possible has only the "alg" specification set to "none")
# - create a claims set (which means create a JSON object)
# - base64 encode the claims set (message and header) and encode them in UTF-8
# - create the JWS by joining the claims set with the period '.' character as a separator

header = {"alg": "none"}
htxt = json.dumps(header)
hdr = b64e(htxt)

claims_set = {"foo": "bar"}
txt = json.dumps(claims_set)
msg = b64e(txt)

jws = ".".join([hdr, msg, ""])

print "jwt:", jws
