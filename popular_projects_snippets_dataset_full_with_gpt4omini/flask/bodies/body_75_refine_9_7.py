from flask import Flask, jsonify, request # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

e = BadRequest('Mock error for testing') # pragma: no cover
BadRequest = type('BadRequest', (Exception,), {}) # pragma: no cover
current_app = Flask(__name__) # pragma: no cover
current_app.debug = True # pragma: no cover

from flask import Flask, jsonify # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

class MyApp:  # Custom app class to allow using super() # pragma: no cover
    def on_json_loading_failed(self, e): # pragma: no cover
        return 'Failed to load JSON' # pragma: no cover
e = Exception('Mock error for testing') # pragma: no cover
BadRequest = MyApp # pragma: no cover
current_app = MyApp() # pragma: no cover

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
