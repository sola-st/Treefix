from flask import Flask # pragma: no cover
from itsdangerous import URLSafeTimedSerializer # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'my_secret_key' # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'key_derivation': 'hmac', # pragma: no cover
    'digest_method': 'sha1', # pragma: no cover
    'salt': 'itsdangerous_salt', # pragma: no cover
    'serializer': None # pragma: no cover
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
