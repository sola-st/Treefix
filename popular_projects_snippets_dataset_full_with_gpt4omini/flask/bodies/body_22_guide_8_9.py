from flask import Flask, session # pragma: no cover
from werkzeug.local import LocalProxy # pragma: no cover

self = type('Mock', (object,), {'app': Flask(__name__), '_cv_tokens': [], 'session': None, 'url_adapter': None})() # pragma: no cover
self.app.secret_key = 'test_secret' # pragma: no cover
self.app.session_interface = type('MockSessionInterface', (object,), {'open_session': lambda app, req: {'valid_session': True}, 'make_null_session': lambda app: {}})() # pragma: no cover
_cv_app = LocalProxy(lambda: self.app) # pragma: no cover
_cv_request = LocalProxy(lambda: 'mock_request') # pragma: no cover
self._cv_tokens = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
# Before we push the request context we have to ensure that there
# is an application context.
from l3.Runtime import _l_
app_ctx = _cv_app.get(None)
_l_(4824)

if app_ctx is None or app_ctx.app is not self.app:
    _l_(4828)

    app_ctx = self.app.app_context()
    _l_(4825)
    app_ctx.push()
    _l_(4826)
else:
    app_ctx = None
    _l_(4827)

self._cv_tokens.append((_cv_request.set(self), app_ctx))
_l_(4829)

# Open the session at the moment that the request context is available.
# This allows a custom open_session method to use the request context.
# Only open a new session if this is the first time the request was
# pushed, otherwise stream_with_context loses the session.
if self.session is None:
    _l_(4834)

    session_interface = self.app.session_interface
    _l_(4830)
    self.session = session_interface.open_session(self.app, self.request)
    _l_(4831)

    if self.session is None:
        _l_(4833)

        self.session = session_interface.make_null_session(self.app)
        _l_(4832)
if self.url_adapter is not None:
    _l_(4836)

    self.match_request()
    _l_(4835)
