from werkzeug.exceptions import BadRequest # pragma: no cover
from flask import current_app # pragma: no cover

e = Exception('Sample Exception') # pragma: no cover
BadRequest = BadRequest # pragma: no cover
current_app = type('Mock', (object,), {'debug': True})() # pragma: no cover

from werkzeug.exceptions import BadRequest # pragma: no cover
from flask import Flask, current_app # pragma: no cover

class CustomClass: # pragma: no cover
    def on_json_loading_failed(self, e): # pragma: no cover
        return 'Error: {}'.format(str(e)) # pragma: no cover
 # pragma: no cover
app = Flask(__name__) # pragma: no cover
app.debug = True # pragma: no cover
with app.app_context(): # pragma: no cover
    current_app = type('Mock', (object,), {'debug': current_app.debug})() # pragma: no cover
    e = Exception('JSON loading error') # pragma: no cover
    BadRequest = BadRequest # pragma: no cover
    current_class_instance = CustomClass() # pragma: no cover
    current_class_instance.on_json_loading_failed(e) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/wrappers.py
from l3.Runtime import _l_
try:
    _l_(22836)

    aux = super().on_json_loading_failed(e)
    _l_(22831)
    exit(aux)
except BadRequest as e:
    _l_(22835)

    if current_app and current_app.debug:
        _l_(22833)

        raise
        _l_(22832)

    raise BadRequest() from e
    _l_(22834)
