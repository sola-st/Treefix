from itsdangerous import URLSafeTimedSerializer # pragma: no cover

class Mock: pass # pragma: no cover
app = Mock() # pragma: no cover
app.secret_key = 'my_secret_key' # pragma: no cover
self = type('MockSelf', (object,), {'key_derivation': 'pbkdf2', 'digest_method': 'sha256', 'salt': 'my_salt', 'serializer': None})() # pragma: no cover
URLSafeTimedSerializer = lambda secret_key, salt, serializer, signer_kwargs: {'secret_key': secret_key, 'salt': salt, 'serializer': serializer, 'signer_kwargs': signer_kwargs} # pragma: no cover

from itsdangerous import URLSafeTimedSerializer # pragma: no cover

class Mock: pass # pragma: no cover
app = Mock() # pragma: no cover
app.secret_key = 'my_secret_key' # pragma: no cover
self = type('MockSelf', (object,), {'key_derivation': 'pbkdf2', 'digest_method': 'sha256', 'salt': 'my_salt', 'serializer': 'json'})() # pragma: no cover
def URLSafeTimedSerializer(secret_key, salt, serializer, signer_kwargs): return {'secret_key': secret_key, 'salt': salt, 'serializer': serializer, 'signer_kwargs': signer_kwargs} # pragma: no cover
signer_kwargs = {'key_derivation': self.key_derivation, 'digest_method': self.digest_method} # pragma: no cover

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
