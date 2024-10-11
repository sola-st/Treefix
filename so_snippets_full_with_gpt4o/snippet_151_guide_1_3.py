import sys # pragma: no cover
import types # pragma: no cover

app = types.ModuleType('app') # pragma: no cover
app.app = type('Mock', (object,), {}) # pragma: no cover
app.abort = lambda *args, **kwargs: None # pragma: no cover
app.make_response = lambda *args, **kwargs: None # pragma: no cover
app.redirect = lambda *args, **kwargs: None # pragma: no cover
app.render_template = lambda *args, **kwargs: None # pragma: no cover
app.request = type('Mock', (object,), {}) # pragma: no cover
app.session = {} # pragma: no cover
sys.modules['app'] = app # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python
from l3.Runtime import _l_
try:
    from app import (
        app, abort, make_response, redirect, render_template, request, session
    )
    _l_(11839)

except ImportError:
    pass

