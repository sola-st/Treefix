from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
current_app.debug = True # pragma: no cover
class MockSelf:  # pragma: no cover
    mimetype = 'application/json' # pragma: no cover
    files = None # pragma: no cover
self = MockSelf() # pragma: no cover

from flask import Flask # pragma: no cover
from werkzeug.datastructures import MultiDict # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
current_app.debug = True # pragma: no cover
class BaseForm:  # pragma: no cover
    def _load_form_data(self): # pragma: no cover
        pass # pragma: no cover
class MockSelf(BaseForm):  # pragma: no cover
    mimetype = 'application/json' # pragma: no cover
    files = None # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/wrappers.py
from l3.Runtime import _l_
super()._load_form_data()
_l_(4323)

# In debug mode we're replacing the files multidict with an ad-hoc
# subclass that raises a different error for key errors.
if (
    current_app
    and current_app.debug
    and self.mimetype != "multipart/form-data"
    and not self.files
):
    _l_(4327)

    try:
        from .debughelpers import attach_enctype_error_multidict
        _l_(4325)

    except ImportError:
        pass

    attach_enctype_error_multidict(self)
    _l_(4326)
