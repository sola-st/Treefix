from flask import current_app, jsonify # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

class MockObject(object): # pragma: no cover
    def on_json_loading_failed(self, e): # pragma: no cover
        return 'Failed to load JSON' # pragma: no cover
         # pragma: no cover
current_app = type('Mock', (object,), {'debug': True})() # pragma: no cover
e = ValueError('Example error') # pragma: no cover

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
