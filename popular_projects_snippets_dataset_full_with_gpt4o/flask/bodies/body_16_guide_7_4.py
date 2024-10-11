import sys # pragma: no cover
from contextvars import ContextVar # pragma: no cover
from blinker import Signal # pragma: no cover

_sentinel = object() # pragma: no cover
_cv_app = ContextVar('app_context') # pragma: no cover
class MockApp: # pragma: no cover
    def do_teardown_appcontext(self, exc): # pragma: no cover
        pass # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._cv_tokens = [_cv_app.set(self)] # pragma: no cover
        self.app = MockApp() # pragma: no cover
self = MockSelf() # pragma: no cover
ctx = object() # pragma: no cover
_cv_app.set(ctx) # pragma: no cover
exc = _sentinel # pragma: no cover
appcontext_popped = Signal('appcontext-popped') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Pops the app context."""
try:
    _l_(22680)

    if len(self._cv_tokens) == 1:
        _l_(22676)

        if exc is _sentinel:
            _l_(22674)

            exc = sys.exc_info()[1]
            _l_(22673)
        self.app.do_teardown_appcontext(exc)
        _l_(22675)
finally:
    _l_(22679)

    ctx = _cv_app.get()
    _l_(22677)
    _cv_app.reset(self._cv_tokens.pop())
    _l_(22678)

if ctx is not self:
    _l_(22682)

    raise AssertionError(
        f"Popped wrong app context. ({ctx!r} instead of {self!r})"
    )
    _l_(22681)

appcontext_popped.send(self.app)
_l_(22683)
