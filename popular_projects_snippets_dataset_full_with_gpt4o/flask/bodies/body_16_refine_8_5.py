import sys # pragma: no cover

self = type('Mock', (object,), {'_cv_tokens': [1], 'app': type('MockApp', (object,), {'do_teardown_appcontext': lambda self, exc: None})()})() # pragma: no cover
exc = None # pragma: no cover
_sentinel = object() # pragma: no cover
_cv_app = type('Mock', (object,), {'get': lambda: 'mock_context', 'reset': lambda x: None})() # pragma: no cover
appcontext_popped = type('Mock', (object,), {'send': lambda app: None})() # pragma: no cover

import sys # pragma: no cover

self = type('MockSelf', (object,), {'_cv_tokens': [1], 'app': type('MockApp', (object,), {'do_teardown_appcontext': lambda self, exc: None})()})() # pragma: no cover
exc = None # pragma: no cover
_sentinel = object() # pragma: no cover
sys.exc_info = lambda: (None, Exception('Sample exception'), None) # pragma: no cover
_cv_app = type('MockCvApp', (object,), {'get': lambda self: self, 'reset': lambda self, token: None})() # pragma: no cover
appcontext_popped = type('MockAppContextPopped', (object,), {'send': lambda self, app: None})() # pragma: no cover

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
