from types import SimpleNamespace # pragma: no cover

app = SimpleNamespace() # pragma: no cover
abort = lambda x: None # pragma: no cover
make_response = lambda x: None # pragma: no cover
redirect = lambda x: None # pragma: no cover
render_template = lambda x: None # pragma: no cover
request = SimpleNamespace() # pragma: no cover
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

