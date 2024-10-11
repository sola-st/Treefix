from http.cookies import SimpleCookie # pragma: no cover
class MockSession: # pragma: no cover
    def __init__(self, modified=False, accessed=False): # pragma: no cover
        self.modified = modified # pragma: no cover
        self.accessed = accessed # pragma: no cover

app = type('MockApp', (), {})() # pragma: no cover
session = MockSession(modified=True, accessed=True) # pragma: no cover
response = type('MockResponse', (), {'delete_cookie': lambda self, name, domain, path, secure, samesite, httponly: None, 'set_cookie': lambda self, name, val, expires, httponly, domain, path, secure, samesite: None, 'vary': set()})() # pragma: no cover
self = type('MockSelf', (), {'get_cookie_name': lambda self, app: 'sessionid', 'get_cookie_domain': lambda self, app: 'example.com', 'get_cookie_path': lambda self, app: '/', 'get_cookie_secure': lambda self, app: True, 'get_cookie_samesite': lambda self, app: 'Lax', 'get_cookie_httponly': lambda self, app: True, 'should_set_cookie': lambda self, app, session: True, 'get_expiration_time': lambda self, app, session: 3600, 'get_signing_serializer': lambda self, app: type('MockSerializer', (), {'dumps': lambda self, data: 'signed_data'})()})() # pragma: no cover

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
