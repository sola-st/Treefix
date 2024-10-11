from typing import Optional # pragma: no cover
from mock import Mock # pragma: no cover

class MockResponse: # Mocking the response object # pragma: no cover
    def __init__(self): # pragma: no cover
        self.cookies = {} # pragma: no cover
        self.vary = set() # pragma: no cover
    def delete_cookie(self, name, domain=None, path=None, secure=None, samesite=None, httponly=None): # pragma: no cover
        self.cookies.pop(name, None) # pragma: no cover
    def set_cookie(self, name, value, expires=None, httponly=None, domain=None, path=None, secure=None, samesite=None): # pragma: no cover
        self.cookies[name] = {'value': value, 'expires': expires, 'httponly': httponly, 'domain': domain, 'path': path, 'secure': secure, 'samesite': samesite} # pragma: no cover
class MockApp: pass # pragma: no cover
class MockSession: # pragma: no cover
    def __init__(self, modified=False, accessed=False): # pragma: no cover
        self.modified = modified # pragma: no cover
        self.accessed = accessed # pragma: no cover
name = 'session_cookie' # pragma: no cover
domain = 'example.com' # pragma: no cover
path = '/' # pragma: no cover
secure = False # pragma: no cover
samesite = 'Lax' # pragma: no cover
httponly = True # pragma: no cover
response = MockResponse() # pragma: no cover
session = MockSession(modified=True, accessed=True) # pragma: no cover
self = Mock() # pragma: no cover
self.get_cookie_name = Mock(return_value=name) # pragma: no cover
self.get_cookie_domain = Mock(return_value=domain) # pragma: no cover
self.get_cookie_path = Mock(return_value=path) # pragma: no cover
self.get_cookie_secure = Mock(return_value=secure) # pragma: no cover
self.get_cookie_samesite = Mock(return_value=samesite) # pragma: no cover
self.get_cookie_httponly = Mock(return_value=httponly) # pragma: no cover
self.should_set_cookie = Mock(return_value=True) # pragma: no cover
self.get_expiration_time = Mock(return_value=None) # pragma: no cover
self.get_signing_serializer = Mock(return_value=Mock(dumps=Mock(return_value='encoded_session'))) # pragma: no cover

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
