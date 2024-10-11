from contextvars import ContextVar # pragma: no cover

_cv_app = ContextVar('app') # pragma: no cover
_cv_request = ContextVar('request') # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self.app = type('MockApp', (object,), {'app_context': lambda: type('AppContext', (object,), {'push': lambda: None})()})() # pragma: no cover
self._cv_tokens = [] # pragma: no cover
self.session = None # pragma: no cover
self.url_adapter = None # pragma: no cover
self.app.session_interface = type('MockSessionInterface', (object,), {'open_session': lambda app, req: None, 'make_null_session': lambda app: None})() # pragma: no cover
self.request = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
# Before we push the request context we have to ensure that there
# is an application context.
from l3.Runtime import _l_
app_ctx = _cv_app.get(None)
_l_(22547)

if app_ctx is None or app_ctx.app is not self.app:
    _l_(22551)

    app_ctx = self.app.app_context()
    _l_(22548)
    app_ctx.push()
    _l_(22549)
else:
    app_ctx = None
    _l_(22550)

self._cv_tokens.append((_cv_request.set(self), app_ctx))
_l_(22552)

# Open the session at the moment that the request context is available.
# This allows a custom open_session method to use the request context.
# Only open a new session if this is the first time the request was
# pushed, otherwise stream_with_context loses the session.
if self.session is None:
    _l_(22557)

    session_interface = self.app.session_interface
    _l_(22553)
    self.session = session_interface.open_session(self.app, self.request)
    _l_(22554)

    if self.session is None:
        _l_(22556)

        self.session = session_interface.make_null_session(self.app)
        _l_(22555)
if self.url_adapter is not None:
    _l_(22559)

    self.match_request()
    _l_(22558)
