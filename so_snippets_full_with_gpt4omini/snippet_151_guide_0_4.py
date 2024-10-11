from flask import Flask, abort, make_response, redirect, render_template, request, session # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'supersecretkey' # pragma: no cover
abort = lambda status_code: (status_code, 'Abort called') # pragma: no cover
make_response = lambda response_data: ('response', response_data) # pragma: no cover
redirect = lambda location: ('redirect', location) # pragma: no cover
render_template = lambda template_name, **context: (template_name, context) # pragma: no cover
request = type('MockRequest', (object,), {'cookies': {}, 'args': {}, 'form': {}})() # pragma: no cover
session = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python
from l3.Runtime import _l_
try:
    from app import (
        app, abort, make_response, redirect, render_template, request, session
    )
    _l_(62)

except ImportError:
    pass

