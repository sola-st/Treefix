import sys # pragma: no cover
from contextlib import contextmanager # pragma: no cover

class App:  # mock class to simulate the app context# pragma: no cover
    def do_teardown_appcontext(self, exc): pass# pragma: no cover
# pragma: no cover
self = type('MockSelf', (object,), {'_cv_tokens': [1], 'app': App()})() # pragma: no cover
exc = type('MockExc', (object,), {})() # pragma: no cover
class MockContext:  # mock class for context lifecycle# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
_cv_app = type('MockCVApp', (object,), {'get': lambda: MockContext(), 'reset': lambda token: None})() # pragma: no cover
_sentinel = object() # pragma: no cover

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
