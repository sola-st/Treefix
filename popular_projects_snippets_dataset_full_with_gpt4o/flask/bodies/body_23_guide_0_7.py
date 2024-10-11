import sys # pragma: no cover
from contextvars import ContextVar # pragma: no cover

_sentinel = object() # pragma: no cover
_cv_request = ContextVar('request') # pragma: no cover
self = type('MockContext', (object,), { # pragma: no cover
'_cv_tokens': [(None, None)], # pragma: no cover
'app': type('MockApp', (object,), { # pragma: no cover
'do_teardown_request': lambda self, exc: None # pragma: no cover
})(), # pragma: no cover
'request': type('MockRequest', (object,), { # pragma: no cover
'close': lambda self: None, # pragma: no cover
'environ': {'werkzeug.request': None} # pragma: no cover
})() # pragma: no cover
})() # pragma: no cover

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
