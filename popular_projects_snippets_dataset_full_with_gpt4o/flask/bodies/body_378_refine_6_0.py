from itsdangerous import URLSafeTimedSerializer # pragma: no cover

app = type('App', (object,), {'secret_key': 'supersecret'})() # pragma: no cover
self = type('Self', (object,), {'key_derivation': 'hmac', 'digest_method': 'sha256', 'salt': 'saltysalt', 'serializer': None})() # pragma: no cover

from itsdangerous import URLSafeTimedSerializer # pragma: no cover
import json # pragma: no cover

app = type('MockApp', (object,), {'secret_key': 'mysecretkey'})() # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'key_derivation': 'hmac', # pragma: no cover
    'digest_method': staticmethod(lambda msg=None: 'sha1'), # pragma: no cover
    'salt': 'mysalt', # pragma: no cover
    'serializer': type('MockSerializer', (object,), {'dumps': staticmethod(json.dumps), 'loads': staticmethod(json.loads)}) # pragma: no cover
})() # pragma: no cover

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
