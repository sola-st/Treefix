from unittest.mock import Mock, MagicMock # pragma: no cover

self = type('Mock', (object,), {'get_cookie_name': Mock(return_value='test_cookie'), 'get_cookie_domain': Mock(return_value='.example.com'), 'get_cookie_path': Mock(return_value='/'), 'get_cookie_secure': Mock(return_value=True), 'get_cookie_samesite': Mock(return_value='Lax'), 'get_cookie_httponly': Mock(return_value=True), 'should_set_cookie': Mock(return_value=True), 'get_expiration_time': Mock(return_value='2024-01-01T00:00:00Z'), 'get_signing_serializer': Mock(return_value=Mock(dumps=Mock(return_value='signed_value')))} )() # pragma: no cover
app = Mock() # pragma: no cover
session = type('Mock', (object,), {'modified': False, 'accessed': False})() # pragma: no cover
response = type('Mock', (object,), {'delete_cookie': Mock(), 'vary': set(), 'set_cookie': Mock()})() # pragma: no cover

from datetime import datetime, timedelta # pragma: no cover
import json # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self, **kwargs): # pragma: no cover
        self.__dict__.update(kwargs) # pragma: no cover
 # pragma: no cover
self = Mock( # pragma: no cover
    get_cookie_name=lambda app: 'sessionid', # pragma: no cover
    get_cookie_domain=lambda app: 'example.com', # pragma: no cover
    get_cookie_path=lambda app: '/', # pragma: no cover
    get_cookie_secure=lambda app: True, # pragma: no cover
    get_cookie_samesite=lambda app: 'Lax', # pragma: no cover
    get_cookie_httponly=lambda app: True, # pragma: no cover
    should_set_cookie=lambda app, session: True, # pragma: no cover
    get_expiration_time=lambda app, session: datetime.utcnow() + timedelta(days=1), # pragma: no cover
    get_signing_serializer=lambda app: type('Serializer', (object,), {'dumps': lambda self, obj: 'signed_value'})() # pragma: no cover
) # pragma: no cover
 # pragma: no cover
app = Mock() # pragma: no cover
 # pragma: no cover
session = Mock( # pragma: no cover
    modified=True, # pragma: no cover
    accessed=True, # pragma: no cover
    items=lambda: [('key', 'value')]  # Add iterable mock data # pragma: no cover
) # pragma: no cover
 # pragma: no cover
response = Mock( # pragma: no cover
    delete_cookie=lambda self, name, domain, path, secure, samesite, httponly: None, # pragma: no cover
    vary=type('MockVary', (object,), {'add': lambda self, value: None})(), # pragma: no cover
    set_cookie=lambda self, name, val, expires, httponly, domain, path, secure, samesite: None # pragma: no cover
) # pragma: no cover

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
