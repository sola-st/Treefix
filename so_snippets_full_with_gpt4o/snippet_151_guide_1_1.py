app = type('Mock', (object,), {})() # pragma: no cover
abort = lambda code: None # pragma: no cover
make_response = lambda content, code: None # pragma: no cover
redirect = lambda url: None # pragma: no cover
render_template = lambda template_name, **context: None # pragma: no cover
request = type('Mock', (object,), {'form': {}, 'args': {}, 'json': {}})() # pragma: no cover
session = {} # pragma: no cover

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

