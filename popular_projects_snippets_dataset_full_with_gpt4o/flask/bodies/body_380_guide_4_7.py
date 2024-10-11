from flask import Flask, session, Response # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'supersecretkey' # pragma: no cover
class MockSelf: # pragma: no cover
    def get_cookie_name(self, app): return 'mock_cookie_name' # pragma: no cover
    def get_cookie_domain(self, app): return 'mock_cookie_domain' # pragma: no cover
    def get_cookie_path(self, app): return '/' # pragma: no cover
    def get_cookie_secure(self, app): return True # pragma: no cover
    def get_cookie_samesite(self, app): return 'Lax' # pragma: no cover
    def get_cookie_httponly(self, app): return True # pragma: no cover
    def should_set_cookie(self, app, session): return False # pragma: no cover
    def get_expiration_time(self, app, session): # pragma: no cover
        return datetime.utcnow() + timedelta(days=1) # pragma: no cover
    def get_signing_serializer(self, app): # pragma: no cover
        class MockSerializer: # pragma: no cover
            def dumps(self, obj): return 'mock_serialized_session' # pragma: no cover
        return MockSerializer() # pragma: no cover
 # pragma: no cover
class MockResponse(Response): # pragma: no cover
    def delete_cookie(self, key, domain=None, path='/', secure=False, samesite=None, httponly=True): # pragma: no cover
        print(f'Deleted cookie {key}') # pragma: no cover
    def set_cookie(self, key, value='', max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None): # pragma: no cover
        print(f'Set cookie {key} = {value}') # pragma: no cover
 # pragma: no cover
session = {} # pragma: no cover
self = MockSelf() # pragma: no cover
response = MockResponse() # pragma: no cover
session.clear() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
name = self.get_cookie_name(app)
_l_(15447)
domain = self.get_cookie_domain(app)
_l_(15448)
path = self.get_cookie_path(app)
_l_(15449)
secure = self.get_cookie_secure(app)
_l_(15450)
samesite = self.get_cookie_samesite(app)
_l_(15451)
httponly = self.get_cookie_httponly(app)
_l_(15452)

# If the session is modified to be empty, remove the cookie.
# If the session is empty, return without setting the cookie.
if not session:
    _l_(15456)

    if session.modified:
        _l_(15454)

        response.delete_cookie(
            name,
            domain=domain,
            path=path,
            secure=secure,
            samesite=samesite,
            httponly=httponly,
        )
        _l_(15453)

    exit()
    _l_(15455)

# Add a "Vary: Cookie" header if the session was accessed at all.
if session.accessed:
    _l_(15458)

    response.vary.add("Cookie")
    _l_(15457)

if not self.should_set_cookie(app, session):
    _l_(15460)

    exit()
    _l_(15459)

expires = self.get_expiration_time(app, session)
_l_(15461)
val = self.get_signing_serializer(app).dumps(dict(session))  # type: ignore
_l_(15462)  # type: ignore
response.set_cookie(
    name,
    val,  # type: ignore
    expires=expires,
    httponly=httponly,
    domain=domain,
    path=path,
    secure=secure,
    samesite=samesite,
)
_l_(15463)
