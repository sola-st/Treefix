from itsdangerous import URLSafeTimedSerializer # pragma: no cover
class MockApp: # pragma: no cover
    secret_key = 'my_secret_key' # pragma: no cover
class MockSelf: # pragma: no cover
    key_derivation = 'hmac' # pragma: no cover
    digest_method = staticmethod(lambda: 'sha1') # pragma: no cover
    salt = 'salt_string' # pragma: no cover
    serializer = 'json' # pragma: no cover

app = MockApp() # pragma: no cover
self = MockSelf() # pragma: no cover

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
