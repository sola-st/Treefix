from flask import current_app # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

e = BadRequest('JSON loading failed') # pragma: no cover
current_app = type('Mock', (object,), {'debug': True})() # pragma: no cover

import sys # pragma: no cover
from flask import current_app # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

e = BadRequest('JSON loading failed') # pragma: no cover
current_app = type('Mock', (object,), {'debug': True})() # pragma: no cover
def super_on_json_loading_failed(e):# pragma: no cover
    print('Mocking super().on_json_loading_failed')# pragma: no cover
    return 'Failed to load JSON' # pragma: no cover
super = lambda: type('SuperMock', (object,), {'on_json_loading_failed': super_on_json_loading_failed})() # pragma: no cover

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
