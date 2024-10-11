from flask import Flask, abort, make_response, redirect, render_template, request, session # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'my_secret_key' # pragma: no cover
abort = lambda code: f'Aborted with status code: {code}' # pragma: no cover
make_response = lambda x: f'Response: {x}' # pragma: no cover
redirect = lambda url: f'Redirected to {url}' # pragma: no cover
render_template = lambda template, **context: f'Rendering {template} with {context}' # pragma: no cover
request = type('MockRequest', (object,), {'args': {}, 'form': {}})() # pragma: no cover
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

