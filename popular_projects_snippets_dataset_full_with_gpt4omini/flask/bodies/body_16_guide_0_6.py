import sys # pragma: no cover
from collections import UserDict # pragma: no cover

class MockApp:  # Mock for app that has do_teardown_appcontext method # pragma: no cover
    def do_teardown_appcontext(self, exc): pass # pragma: no cover
 # pragma: no cover
class MockContextVar(UserDict):  # Mock for context variables # pragma: no cover
    def __init__(self): # pragma: no cover
        super().__init__() # pragma: no cover
        self._tokens = [] # pragma: no cover
     # pragma: no cover
    def get(self): # pragma: no cover
        return self.data.get('current_app') # pragma: no cover
     # pragma: no cover
    def reset(self, token): # pragma: no cover
        self._tokens.remove(token) # pragma: no cover
        self.data['current_app'] = None # pragma: no cover
        if token == 'token1':  # example token # pragma: no cover
            self.data['current_app'] = MockApp() # pragma: no cover
        return self.data['current_app'] # pragma: no cover
 # pragma: no cover
self = MockApp() # pragma: no cover
self._cv_tokens = ['token1'] # pragma: no cover
self.app = MockApp() # pragma: no cover
exc = 'error' # pragma: no cover
_cv_app = MockContextVar() # pragma: no cover
_cv_app.data['current_app'] = self.app # pragma: no cover

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
