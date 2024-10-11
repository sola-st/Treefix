current_app = type('Mock', (object,), {'debug': True})() # pragma: no cover
self = type('Mock', (object,), {'mimetype': 'application/json', 'files': False})() # pragma: no cover

current_app = type('MockApp', (object,), {'debug': True})() # pragma: no cover
self = type('MockRequest', (object,), {'mimetype': 'application/json', 'files': {}, '_load_form_data': lambda: None})() # pragma: no cover

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
