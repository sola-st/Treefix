import sys # pragma: no cover
from contextvars import ContextVar # pragma: no cover

class MockApp: # pragma: no cover
    def do_teardown_request(self, exc): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockRequest: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.environ = {'werkzeug.request': 'request_data'} # pragma: no cover
    def close(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockAppCtx: # pragma: no cover
    def pop(self, exc): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.app = MockApp() # pragma: no cover
        self.request = MockRequest() # pragma: no cover
        self._cv_tokens = [(None, MockAppCtx())] # pragma: no cover
    def __repr__(self): # pragma: no cover
        return '<MockSelf>' # pragma: no cover
 # pragma: no cover
_cv_request = ContextVar('request_context') # pragma: no cover
_sentinel = object() # pragma: no cover
def mock_reset(token): # pragma: no cover
    pass # pragma: no cover
_cv_request.set(MockSelf()) # pragma: no cover
sys.exc_info = lambda: (None, Exception('example_exception'), None) # pragma: no cover
self = _cv_request.get() # pragma: no cover
ctx = type('MockWrongContext', (object,), { # pragma: no cover
    'request': type('MockRequest', (object,), { # pragma: no cover
        'environ': {'werkzeug.request': 'another_request'} # pragma: no cover
    })(), # pragma: no cover
})() # pragma: no cover
_cv_request.set(ctx) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Pops the request context and unbinds it by doing that.  This will
        also trigger the execution of functions registered by the
        :meth:`~flask.Flask.teardown_request` decorator.

        .. versionchanged:: 0.9
           Added the `exc` argument.
        """
clear_request = len(self._cv_tokens) == 1
_l_(22766)

try:
    _l_(22784)

    if clear_request:
        _l_(22773)

        if exc is _sentinel:
            _l_(22768)

            exc = sys.exc_info()[1]
            _l_(22767)
        self.app.do_teardown_request(exc)
        _l_(22769)

        request_close = getattr(self.request, "close", None)
        _l_(22770)
        if request_close is not None:
            _l_(22772)

            request_close()
            _l_(22771)
finally:
    _l_(22783)

    ctx = _cv_request.get()
    _l_(22774)
    token, app_ctx = self._cv_tokens.pop()
    _l_(22775)
    _cv_request.reset(token)
    _l_(22776)

    # get rid of circular dependencies at the end of the request
    # so that we don't require the GC to be active.
    if clear_request:
        _l_(22778)

        ctx.request.environ["werkzeug.request"] = None
        _l_(22777)

    if app_ctx is not None:
        _l_(22780)

        app_ctx.pop(exc)
        _l_(22779)

    if ctx is not self:
        _l_(22782)

        raise AssertionError(
            f"Popped wrong request context. ({ctx!r} instead of {self!r})"
        )
        _l_(22781)
