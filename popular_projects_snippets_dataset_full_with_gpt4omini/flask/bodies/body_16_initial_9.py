import sys # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock(app=Mock(), _cv_tokens=[1], __class__=type('AppContext', (), {})) # pragma: no cover
exc = None # pragma: no cover
_sentinel = object() # pragma: no cover
sys = Mock(exc_info=lambda: (None, 'some_exception', None)) # pragma: no cover
_cv_app = Mock(get=lambda: self, reset=lambda token: None) # pragma: no cover
appcontext_popped = Mock(send=lambda app: None) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Pops the app context."""
try:
    _l_(6042)

    if len(self._cv_tokens) == 1:
        _l_(6038)

        if exc is _sentinel:
            _l_(6036)

            exc = sys.exc_info()[1]
            _l_(6035)
        self.app.do_teardown_appcontext(exc)
        _l_(6037)
finally:
    _l_(6041)

    ctx = _cv_app.get()
    _l_(6039)
    _cv_app.reset(self._cv_tokens.pop())
    _l_(6040)

if ctx is not self:
    _l_(6044)

    raise AssertionError(
        f"Popped wrong app context. ({ctx!r} instead of {self!r})"
    )
    _l_(6043)

appcontext_popped.send(self.app)
_l_(6045)
