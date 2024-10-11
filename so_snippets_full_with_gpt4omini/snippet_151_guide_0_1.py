from flask import Flask, abort, make_response, redirect, render_template, request, session # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'my_secret_key' # pragma: no cover
abort = type('Mock', (object,), {})() # pragma: no cover
make_response = type('Mock', (object,), {'__call__': lambda self, x: x})() # pragma: no cover
redirect = type('Mock', (object,), {'__call__': lambda self, url: f'Redirected to {url}'})() # pragma: no cover
render_template = type('Mock', (object,), {'__call__': lambda self, template, **context: f'Rendered {template} with {context}'})() # pragma: no cover
request = type('Mock', (object,), {'args': {}})() # pragma: no cover
session = type('Mock', (object,), {'data': {}})() # pragma: no cover

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

