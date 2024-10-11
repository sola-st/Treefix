import sys # pragma: no cover
from contextvars import ContextVar # pragma: no cover
from flask.signals import appcontext_popped # pragma: no cover

class Sentinel: pass # pragma: no cover
_sentinel = Sentinel() # pragma: no cover
_cv_app = ContextVar('current_app_context') # pragma: no cover
self = type('Mock', (object,), {'_cv_tokens': [1], 'app': type('MockApp', (object,), {'do_teardown_appcontext': lambda self, exc: None})()})() # pragma: no cover
self._cv_tokens = ['token'] # pragma: no cover
self._cv_tokens.append('second_token') # pragma: no cover

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
