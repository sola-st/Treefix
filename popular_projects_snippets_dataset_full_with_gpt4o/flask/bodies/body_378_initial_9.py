from itsdangerous import URLSafeTimedSerializer # pragma: no cover

app = type('Mock', (object,), {'secret_key': 'supersecret'})() # pragma: no cover
self = type('Mock', (object,), {'key_derivation': 'hmac', 'digest_method': staticmethod(lambda x: x), 'salt': 'mysalt', 'serializer': staticmethod(lambda x: x)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
if not app.secret_key:
    _l_(18232)

    aux = None
    _l_(18231)
    exit(aux)
signer_kwargs = dict(
    key_derivation=self.key_derivation, digest_method=self.digest_method
)
_l_(18233)
aux = URLSafeTimedSerializer(
    app.secret_key,
    salt=self.salt,
    serializer=self.serializer,
    signer_kwargs=signer_kwargs,
)
_l_(18234)
exit(aux)
