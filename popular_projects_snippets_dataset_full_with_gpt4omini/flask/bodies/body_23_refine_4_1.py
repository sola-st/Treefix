import sys # pragma: no cover
from flask import Flask, request, g # pragma: no cover
import threading # pragma: no cover

self = type('Mock', (object,), {'_cv_tokens': [(1, 'app_context')], 'app': Flask(__name__), 'request': request})() # pragma: no cover
exc = None # pragma: no cover
_sentinel = object() # pragma: no cover
sys = type('Mock', (object,), {'exc_info': lambda: (None, 'Exception', None)})() # pragma: no cover
_cv_request = type('Mock', (object,), {'get': lambda: 'context', 'reset': lambda token: None})() # pragma: no cover

import sys # pragma: no cover
from flask import Flask, request, g # pragma: no cover

self = type('Mock', (object,), {'_cv_tokens': [(1, 'app_context')], 'app': Flask(__name__), 'request': request})() # pragma: no cover
exc = None # pragma: no cover
_sentinel = object() # pragma: no cover
sys = type('MockSys', (object,), {'exc_info': lambda: (None, 'Exception', None)})() # pragma: no cover
_cv_request = type('MockCVRequest', (object,), {'_stack': [], 'get': lambda self: self._stack[-1] if self._stack else None, 'reset': lambda self, token: self._stack.pop() if self._stack else None})() # pragma: no cover
_cv_request._stack.append(self) # pragma: no cover

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
_l_(7178)

try:
    _l_(7196)

    if clear_request:
        _l_(7185)

        if exc is _sentinel:
            _l_(7180)

            exc = sys.exc_info()[1]
            _l_(7179)
        self.app.do_teardown_request(exc)
        _l_(7181)

        request_close = getattr(self.request, "close", None)
        _l_(7182)
        if request_close is not None:
            _l_(7184)

            request_close()
            _l_(7183)
finally:
    _l_(7195)

    ctx = _cv_request.get()
    _l_(7186)
    token, app_ctx = self._cv_tokens.pop()
    _l_(7187)
    _cv_request.reset(token)
    _l_(7188)

    # get rid of circular dependencies at the end of the request
    # so that we don't require the GC to be active.
    if clear_request:
        _l_(7190)

        ctx.request.environ["werkzeug.request"] = None
        _l_(7189)

    if app_ctx is not None:
        _l_(7192)

        app_ctx.pop(exc)
        _l_(7191)

    if ctx is not self:
        _l_(7194)

        raise AssertionError(
            f"Popped wrong request context. ({ctx!r} instead of {self!r})"
        )
        _l_(7193)
