from flask import Flask, jsonify, request # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

e = Exception('Loading failed') # pragma: no cover
BadRequest = type('BadRequest', (Exception,), {}) # pragma: no cover
current_app = type('Mock', (object,), {'debug': True})() # pragma: no cover

from flask import Flask, jsonify, Blueprint # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

class MockBlueprint(Blueprint):# pragma: no cover
    def on_json_loading_failed(self, e):# pragma: no cover
        return 'Loading failed', 400 # pragma: no cover
e = Exception('Mock loading error') # pragma: no cover
BadRequest = type('MockBadRequest', (BadRequest,), {}) # pragma: no cover
current_app = type('Mock', (object,), {'debug': True})() # pragma: no cover

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
