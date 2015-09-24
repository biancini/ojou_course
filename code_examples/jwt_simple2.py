#!/usr/bin/env python

from jwkest import b64d
from jwkest.jws import JWS

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
#
# Using the jwkest library the JWT can be created as follow.

jwt = JWS({"foo": "bar"}, alg="none").sign_compact()
print "jwt:", jwt
print

for p in jwt.split('.'):
    p = p.encode("utf8")
    print "-", type(p), b64d(p)