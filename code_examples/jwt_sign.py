#!/usr/bin/env python

from jwkest.jwk import import_rsa_key_from_file
from jwkest.jwk import RSAKey
from jwkest.jwt import JWT
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
# A signed JWT is called JWS. The JWS can be encrypted with different algorithms and of course with different keys.
# To test the mechanism, let's assume you have a file foo with a private RSA key. If you don't have it you can simply
# create one. On linux, just type in the project folder the following command:
# $ ssh-keygen -t rsa -b 4096
# and provide the foo filename with requested.
#
# Now a JWS can be created as follow:
# - retrieve the rsa key (the example below will also print it in the JWK section)
# - use the JWS object to create the token specifying the algorithm to be used for signing
# - call the method sign_compact providing an array of keys (eventually containing 1 key only) to be used for signing
# - the example belows shows the content of the JWT, by printing it
# - the signature can be verified with the method verify_compact (of course providing the same keys used for signing)

payload = {"iss": "jow",
           "exp": 1300819380,
           "http://example.com/is_root": True}

keys = [RSAKey(key=import_rsa_key_from_file("foo"))]
jws = JWS(payload, alg="RS512").sign_compact(keys)
print "jwt signed:", jws
print

########################################

jwt_received = JWT()
jwt_received.unpack(jws)
print "jwt headers:", jwt_received.headers
print "jwt part 1:", jwt_received.part[1]
print

_rj = JWS()
info = _rj.verify_compact(jws, keys)
print "Verified info:", info
