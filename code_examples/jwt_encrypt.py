#!/usr/bin/env python

from Crypto.PublicKey import RSA
from jwkest.jwe import JWE_RSA

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
# A JSON web token encrypted (JWE) can e used to encrypt a message so that it can be read only with a specific key.
# The example will provide two different examples of how to encrypt (and decrypt) a token.
# A JWE can be created as follow:
# - create a JWE_RSA object with the message, the encryption algorithm and the encoding to be used
# - call the encrypt method on this oject passing as an argument the key to be used
# - the example will show the various part of the JWT, which are non decodable with b64, since they're encrypted
#
# A JWE can then be decrypted as follow:
# - create a JWE_RSA object
# - call the decrypt method passing the JWE and the key to be used for decription

rsa = RSA.generate(4096)
plain = "Now is the time for all good men to come to the aid of their country."

_rsa15_enc = JWE_RSA(plain, alg="RSA1_5", enc="A128CBC-HS256")
jwt1 = _rsa15_enc.encrypt(rsa)

print "(1)"
for p in jwt1.split('.'):
    print "-", p

_rsa15_dec = JWE_RSA()
msg = _rsa15_dec.decrypt(jwt1, rsa)
print
print msg

###############################################

_rsaoaep_enc = JWE_RSA(plain, alg="RSA-OAEP", enc="A256GCM")
jwt2 = _rsaoaep_enc.encrypt(rsa)

print "(2)"
for p in jwt2.split('.'):
    print "-", p

_rsaoaep_dec = JWE_RSA()
msg = _rsaoaep_dec.decrypt(jwt2, rsa)
print
print msg
