import types # pragma: no cover

app = type('Mock', (object,), {}) # pragma: no cover
abort = type('Mock', (object,), {'__call__': lambda self, code: None})() # pragma: no cover
make_response = type('Mock', (object,), {'__call__': lambda self, content: None})() # pragma: no cover
redirect = type('Mock', (object,), {'__call__': lambda self, url: None})() # pragma: no cover
render_template = type('Mock', (object,), {'__call__': lambda self, template_name: None})() # pragma: no cover
request = type('Mock', (object,), {'__call__': lambda self: None})() # pragma: no cover
session = type('Mock', (object,), {})() # pragma: no cover

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

