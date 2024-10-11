from flask import current_app # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

e = Exception('Loading Failed') # pragma: no cover
BadRequest = type('MockBadRequest', (BadRequest,), {}) # pragma: no cover
current_app = type('MockCurrentApp', (object,), {'debug': True})() # pragma: no cover

from flask import Flask, current_app # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

class Base: pass # pragma: no cover
class MockLoader(Base): # pragma: no cover
    def on_json_loading_failed(self, e): # pragma: no cover
        return 'Loading failed' # pragma: no cover
e = Exception('Loading failed') # pragma: no cover
BadRequest = BadRequest # pragma: no cover
app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
current_app.debug = True # pragma: no cover
mock_loader = MockLoader() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/wrappers.py
from l3.Runtime import _l_
try:
    _l_(7703)

    aux = super().on_json_loading_failed(e)
    _l_(7698)
    exit(aux)
except BadRequest as e:
    _l_(7702)

    if current_app and current_app.debug:
        _l_(7700)

        raise
        _l_(7699)

    raise BadRequest() from e
    _l_(7701)
