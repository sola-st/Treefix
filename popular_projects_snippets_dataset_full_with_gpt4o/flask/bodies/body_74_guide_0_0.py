from flask import Flask, Request, current_app # pragma: no cover

class MockRequest(Request): # pragma: no cover
    @staticmethod # pragma: no cover
    def _load_form_data(): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
app = Flask(__name__) # pragma: no cover
app.debug = True # pragma: no cover
 # pragma: no cover
with app.app_context(): # pragma: no cover
 # pragma: no cover
    current_app = app # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/wrappers.py
from l3.Runtime import _l_
super()._load_form_data()
_l_(22497)

# In debug mode we're replacing the files multidict with an ad-hoc
# subclass that raises a different error for key errors.
if (
    current_app
    and current_app.debug
    and self.mimetype != "multipart/form-data"
    and not self.files
):
    _l_(22501)

    try:
        from .debughelpers import attach_enctype_error_multidict
        _l_(22499)

    except ImportError:
        pass

    attach_enctype_error_multidict(self)
    _l_(22500)
