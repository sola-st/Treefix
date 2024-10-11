import sys # pragma: no cover
from contextlib import contextmanager # pragma: no cover

class MockApp:  # Mock class to simulate app behavior# pragma: no cover
    def do_teardown_appcontext(self, exc):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockContext:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
class MockCVApp:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.token = 'token'# pragma: no cover
# pragma: no cover
    def get(self):# pragma: no cover
        return MockContext()  # Simulating context retrieval# pragma: no cover
    # pragma: no cover
    def reset(self, token):# pragma: no cover
        pass# pragma: no cover
self = type('MockContextManager', (object,), {})()  # Create a new mock context manager# pragma: no cover
self._cv_tokens = ['token']  # Initialize the context tokens# pragma: no cover
# pragma: no cover
_sentinel = object()  # Define a sentinel object for comparison# pragma: no cover
ctx = None  # ctx variable initialized# pragma: no cover
exc = _sentinel  # exc variable initialized # pragma: no cover

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
