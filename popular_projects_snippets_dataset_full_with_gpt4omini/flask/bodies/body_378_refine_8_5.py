from flask import Flask # pragma: no cover
from itsdangerous import URLSafeTimedSerializer # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'supersecretkey' # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.key_derivation = 'pbkdf2' # pragma: no cover
self.digest_method = 'sha256' # pragma: no cover
self.salt = 'salt' # pragma: no cover
self.serializer = None # pragma: no cover

from flask import Flask # pragma: no cover
from itsdangerous import URLSafeTimedSerializer # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'supersecretkey' # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.key_derivation = 'pbkdf2' # pragma: no cover
self.digest_method = 'sha256' # pragma: no cover
self.salt = 'my_salt' # pragma: no cover
self.serializer = 'json' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
if not app.secret_key:
    _l_(7018)

    aux = None
    _l_(7017)
    exit(aux)
signer_kwargs = dict(
    key_derivation=self.key_derivation, digest_method=self.digest_method
)
_l_(7019)
aux = URLSafeTimedSerializer(
    app.secret_key,
    salt=self.salt,
    serializer=self.serializer,
    signer_kwargs=signer_kwargs,
)
_l_(7020)
exit(aux)
