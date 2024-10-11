from flask import Flask, current_app # pragma: no cover

class MockRequest(type('Mock', (object,), {})): pass # pragma: no cover
app = Flask(__name__) # pragma: no cover
with app.app_context(): # pragma: no cover
    class MockRequest(type('Mock', (object,), {'_load_form_data': lambda self: None})): pass # pragma: no cover
    mock_request = MockRequest() # pragma: no cover
    mock_request.mimetype = 'application/x-www-form-urlencoded' # pragma: no cover
    mock_request.files = None # pragma: no cover
    mock_request._load_form_data = lambda: None # pragma: no cover
    current_app.debug = True # pragma: no cover

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
