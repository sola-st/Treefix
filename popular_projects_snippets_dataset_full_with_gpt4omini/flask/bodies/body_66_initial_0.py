from flask import Flask, request # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.dispatch_request = lambda **kwargs: 'Response from dispatch_request' # pragma: no cover
kwargs = {'param1': 'value1', 'param2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/views.py
from l3.Runtime import _l_
aux = current_app.ensure_sync(self.dispatch_request)(**kwargs)
_l_(5362)
exit(aux)
