from datetime import timedelta # pragma: no cover
from itsdangerous import URLSafeTimedSerializer # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.get_cookie_name = lambda app: 'test_cookie' # pragma: no cover
self.get_cookie_domain = lambda app: 'example.com' # pragma: no cover
self.get_cookie_path = lambda app: '/' # pragma: no cover
self.get_cookie_secure = lambda app: True # pragma: no cover
self.get_cookie_samesite = lambda app: 'Lax' # pragma: no cover
self.get_cookie_httponly = lambda app: True # pragma: no cover
self.should_set_cookie = lambda app, session: True # pragma: no cover
self.get_expiration_time = lambda app, session: (datetime.now() + timedelta(days=1)).timestamp() # pragma: no cover
self.get_signing_serializer = lambda app: URLSafeTimedSerializer('secret') # pragma: no cover
class Session: pass # pragma: no cover
session = Session() # pragma: no cover
session.modified = True # pragma: no cover
session.accessed = True # pragma: no cover
session.data = {'key': 'value'} # pragma: no cover
class Vary: pass # pragma: no cover
response = Mock() # pragma: no cover
response.delete_cookie = lambda name, domain, path, secure, samesite, httponly: None # pragma: no cover
response.vary = Vary() # pragma: no cover
response.vary.add = lambda header: None # pragma: no cover
response.set_cookie = lambda name, val, expires, httponly, domain, path, secure, samesite: None # pragma: no cover

from datetime import datetime, timedelta # pragma: no cover
from flask import Flask, make_response # pragma: no cover

class Mock:# pragma: no cover
    pass # pragma: no cover
self = Mock() # pragma: no cover
self.get_cookie_name = lambda app: 'session_cookie' # pragma: no cover
self.get_cookie_domain = lambda app: 'example.com' # pragma: no cover
self.get_cookie_path = lambda app: '/' # pragma: no cover
self.get_cookie_secure = lambda app: True # pragma: no cover
self.get_cookie_samesite = lambda app: 'Lax' # pragma: no cover
self.get_cookie_httponly = lambda app: True # pragma: no cover
self.should_set_cookie = lambda app, session: True # pragma: no cover
self.get_expiration_time = lambda app, session: (datetime.utcnow() + timedelta(days=1)).strftime('%a, %d-%b-%Y %H:%M:%S GMT') # pragma: no cover
app = Flask(__name__) # pragma: no cover
session = type('MockSession', (object,), {'modified': True, 'accessed': True})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
name = self.get_cookie_name(app)
_l_(3862)
domain = self.get_cookie_domain(app)
_l_(3863)
path = self.get_cookie_path(app)
_l_(3864)
secure = self.get_cookie_secure(app)
_l_(3865)
samesite = self.get_cookie_samesite(app)
_l_(3866)
httponly = self.get_cookie_httponly(app)
_l_(3867)

# If the session is modified to be empty, remove the cookie.
# If the session is empty, return without setting the cookie.
if not session:
    _l_(3871)

    if session.modified:
        _l_(3869)

        response.delete_cookie(
            name,
            domain=domain,
            path=path,
            secure=secure,
            samesite=samesite,
            httponly=httponly,
        )
        _l_(3868)

    exit()
    _l_(3870)

# Add a "Vary: Cookie" header if the session was accessed at all.
if session.accessed:
    _l_(3873)

    response.vary.add("Cookie")
    _l_(3872)

if not self.should_set_cookie(app, session):
    _l_(3875)

    exit()
    _l_(3874)

expires = self.get_expiration_time(app, session)
_l_(3876)
val = self.get_signing_serializer(app).dumps(dict(session))  # type: ignore
_l_(3877)  # type: ignore
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
_l_(3878)
