from werkzeug.exceptions import BadRequest # pragma: no cover
from flask import current_app # pragma: no cover

class MockSuper: # pragma: no cover
    def on_json_loading_failed(self, e): # pragma: no cover
        return 'mocked_aux' # pragma: no cover
class MockApp: # pragma: no cover
    debug = True # pragma: no cover
super = lambda: MockSuper() # pragma: no cover
e = BadRequest('mocked exception') # pragma: no cover
current_app = MockApp() # pragma: no cover

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
