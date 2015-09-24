#!/usr/bin/env python

import json
from oic.utils.keyio import create_and_store_rsa_key_pair, build_keyjar
from jwkest.jwk import RSAKey, KEYS, keyitems2keyreps

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
# Special examples of a JWT are the JWK and the JWKS. The first will represent a key (to be used for signing or
# encryption) the second will represent a keystore containing multiple keys.
# This example will create and print both of them, it can be executed without the need to create a foo RSA key because
# the library will take care of creating it.
#
# Now a JWK can be created as follow:
# - retrieve the rsa key
# - create a RSAKey object, and load the key with the load_key method
#
# A JWKS can instead be created as follow:
# - retrieve the rsa key
# - create a KEYS object and add the keys specifying the algorithm used for creation and the usage allowed for the key
#   (signature or encryption)
#
# A key jar can also be created with the method build_keyjar specifying a key_conf containing a list of keys to be
# created, with their type, name and usage (encryption of signature)

key = create_and_store_rsa_key_pair("foo", size=4096)
key2 = create_and_store_rsa_key_pair("foo2", size=4096)
rsa = RSAKey().load_key(key)

print "--- JWK ---"
print json.dumps(rsa.serialize(), sort_keys=True, indent=4, separators=(',', ': '))
print

########################################################

keys = KEYS()
keys.wrap_add(key, use="sig", kid="rsa1")
keys.wrap_add(key2, use="enc", kid="rsa1")

print "--- JWKS---"
print keys.dump_jwks()
print

########################################################

key_conf = [
    {"type": "RSA", "name": "rsa_key", "use": ["enc", "sig"]},
    {"type": "EC", "name": "elliptic_curve_1", "crv": "P-256", "use": ["sig"]},
    {"type": "EC", "name": "elliptic_curve_2", "crv": "P-256", "use": ["enc"]}
]
jwks, keyjar, kdd = build_keyjar(key_conf, "m%d", None, None)

print "--- JWKS from keyjar ---"
print jwks