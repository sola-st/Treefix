from itsdangerous import URLSafeTimedSerializer # pragma: no cover

class MockApp: secret_key = 'my_secret_key' # pragma: no cover
app = MockApp() # pragma: no cover

from itsdangerous import URLSafeTimedSerializer # pragma: no cover

class MockApp: secret_key = 'my_secret_key' # pragma: no cover
app = MockApp() # pragma: no cover
class MockSelf: key_derivation = 'pbkdf2:sha256'; digest_method = 'sha256'; salt = 'my_salt'; serializer = None # pragma: no cover
self = MockSelf() # pragma: no cover
def init_url_safe_timed_serializer(secret_key, salt, serializer, signer_kwargs): return {'secret_key': secret_key, 'salt': salt, 'serializer': serializer, 'signer_kwargs': signer_kwargs} # pragma: no cover
URLSafeTimedSerializer = init_url_safe_timed_serializer # pragma: no cover

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
