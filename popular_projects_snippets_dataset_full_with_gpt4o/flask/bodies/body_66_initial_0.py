from flask import Flask, current_app # pragma: no cover
class MockFlaskApp(Flask): # pragma: no cover
    def ensure_sync(self, func): # pragma: no cover
        return func # pragma: no cover
class MockSelf: # pragma: no cover
    def dispatch_request(self, **kwargs): # pragma: no cover
        return 'dispatched with ' + str(kwargs) # pragma: no cover

current_app = MockFlaskApp(__name__) # pragma: no cover
self = MockSelf() # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/views.py
from l3.Runtime import _l_
aux = current_app.ensure_sync(self.dispatch_request)(**kwargs)
_l_(22605)
exit(aux)
