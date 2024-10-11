import sys # pragma: no cover
from unittest.mock import Mock, MagicMock # pragma: no cover

class MockApp:# pragma: no cover
    def do_teardown_appcontext(self, exc): pass # pragma: no cover
self = type('MockSelf', (object,), {'_cv_tokens': [1], 'app': MockApp()})() # pragma: no cover
exc = _sentinel = object() # pragma: no cover
_cv_app = Mock() # pragma: no cover
_cv_app.get.return_value = object()  # Simulate ctx is not self # pragma: no cover
_cv_app.reset = Mock() # pragma: no cover
appcontext_popped = MagicMock() # pragma: no cover

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
