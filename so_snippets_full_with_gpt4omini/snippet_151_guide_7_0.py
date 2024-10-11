from flask import Flask, abort, make_response, redirect, render_template, request, session # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'example_secret_key' # pragma: no cover
abort = type('MockAbort', (object,), {'__call__': lambda self, code: 'Aborted with code: ' + str(code)})() # pragma: no cover
make_response = type('MockMakeResponse', (object,), {'__call__': lambda self, data: 'Response: ' + str(data)})() # pragma: no cover
redirect = type('MockRedirect', (object,), {'__call__': lambda self, url: 'Redirected to: ' + url})() # pragma: no cover
render_template = type('MockRenderTemplate', (object,), {'__call__': lambda self, template, **context: 'Rendered ' + template + ' with context: ' + str(context)})() # pragma: no cover
request = type('MockRequest', (object,), {'args': {}})() # pragma: no cover
session = type('MockSession', (object,), {'data': {}})() # pragma: no cover

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

