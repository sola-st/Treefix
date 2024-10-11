from itsdangerous import URLSafeTimedSerializer # pragma: no cover

app = type('AppMock', (object,), {'secret_key': 'mysecretkey'})() # pragma: no cover
self = type('SelfMock', (object,), {'key_derivation': 'hmac', 'digest_method': 'sha1', 'salt': 'somesalt', 'serializer': None})() # pragma: no cover

from itsdangerous import URLSafeTimedSerializer, Serializer # pragma: no cover

app = type('AppMock', (object,), {'secret_key': 'mysecretkey'})() # pragma: no cover
class JSONSerializer(Serializer):# pragma: no cover
    def dumps(self, obj):# pragma: no cover
        return json.dumps(obj)# pragma: no cover
# pragma: no cover
    def loads(self, s):# pragma: no cover
        return json.loads(s) # pragma: no cover

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
