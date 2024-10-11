from flask import Flask, session, Response as FlaskResponse # pragma: no cover
from typing import Any # pragma: no cover
from datetime import datetime, timedelta # pragma: no cover

class MockApp: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
    def get_cookie_name(self, app: Any) -> str: # pragma: no cover
        return 'mock_cookie_name' # pragma: no cover
 # pragma: no cover
    def get_cookie_domain(self, app: Any) -> str: # pragma: no cover
        return 'mock_cookie_domain' # pragma: no cover
 # pragma: no cover
    def get_cookie_path(self, app: Any) -> str: # pragma: no cover
        return '/' # pragma: no cover
 # pragma: no cover
    def get_cookie_secure(self, app: Any) -> bool: # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
    def get_cookie_samesite(self, app: Any) -> str: # pragma: no cover
        return 'Lax' # pragma: no cover
 # pragma: no cover
    def get_cookie_httponly(self, app: Any) -> bool: # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
    def should_set_cookie(self, app: Any, session: Any) -> bool: # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
    def get_expiration_time(self, app: Any, session: Any) -> datetime: # pragma: no cover
        return datetime.utcnow() + timedelta(days=1) # pragma: no cover
 # pragma: no cover
    def get_signing_serializer(self, app: Any): # pragma: no cover
        class MockSerializer: # pragma: no cover
            def dumps(self, obj: dict) -> str: # pragma: no cover
                return 'mock_serialized_session' # pragma: no cover
 # pragma: no cover
        return MockSerializer() # pragma: no cover
 # pragma: no cover
class MockResponse: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.headers = {} # pragma: no cover
        self.cookies = {} # pragma: no cover
        self.vary = set() # pragma: no cover
 # pragma: no cover
    def set_cookie(self, key: str, value: str, **kwargs) -> None: # pragma: no cover
        self.cookies[key] = value # pragma: no cover
 # pragma: no cover
    def delete_cookie(self, key: str, **kwargs) -> None: # pragma: no cover
        if key in self.cookies: # pragma: no cover
            del self.cookies[key] # pragma: no cover
 # pragma: no cover
app = Flask(__name__) # pragma: no cover
self = MockApp() # pragma: no cover
response = MockResponse() # pragma: no cover

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
