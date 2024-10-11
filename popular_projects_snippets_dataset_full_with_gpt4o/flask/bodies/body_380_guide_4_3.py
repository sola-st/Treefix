from flask import Flask, session, Response # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'supersecretkey' # pragma: no cover
response = type('MockResponse', (object,), { # pragma: no cover
    'vary': set(), # pragma: no cover
    'delete_cookie': lambda self, name, domain=None, path='/', secure=False, samesite=None, httponly=True: print(f'Deleted cookie: {name}'), # pragma: no cover
    'set_cookie': lambda self, name, value, expires=None, domain=None, path='/', secure=False, samesite=None, httponly=True: print(f'Set cookie: {name} with value: {value}') # pragma: no cover
})() # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'get_cookie_name': lambda self, app: 'session_cookie', # pragma: no cover
    'get_cookie_domain': lambda self, app: 'example.com', # pragma: no cover
    'get_cookie_path': lambda self, app: '/', # pragma: no cover
    'get_cookie_secure': lambda self, app: True, # pragma: no cover
    'get_cookie_samesite': lambda self, app: 'Lax', # pragma: no cover
    'get_cookie_httponly': lambda self, app: True, # pragma: no cover
    'should_set_cookie': lambda self, app, session: False, # pragma: no cover
    'get_expiration_time': lambda self, app, session: None, # pragma: no cover
    'get_signing_serializer': lambda self, app: type('MockSerializer', (object,), { # pragma: no cover
        'dumps': lambda self, data: 'signed_value' # pragma: no cover
    })() # pragma: no cover
})() # pragma: no cover

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
