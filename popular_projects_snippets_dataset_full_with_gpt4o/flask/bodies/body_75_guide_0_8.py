from flask import Flask, json, current_app # pragma: no cover
from werkzeug.exceptions import BadRequest # pragma: no cover

class MockApp:# pragma: no cover
    debug = True# pragma: no cover
current_app = MockApp() # pragma: no cover
class MockSuper:# pragma: no cover
    def on_json_loading_failed(self, e):# pragma: no cover
        return 'failed'# pragma: no cover
super_obj = MockSuper() # pragma: no cover
class MockBase:# pragma: no cover
    def __init__(self, super_obj):# pragma: no cover
        self.super = super_obj# pragma: no cover
# pragma: no cover
    def __getattribute__(self, name):# pragma: no cover
        if name == 'super':# pragma: no cover
            return super_obj# pragma: no cover
        return object.__getattribute__(self, name) # pragma: no cover
e = BadRequest(description='Error') # pragma: no cover

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
