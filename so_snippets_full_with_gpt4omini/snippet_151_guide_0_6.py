from flask import Flask, abort, make_response, redirect, render_template, request, session # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'supersecretkey' # pragma: no cover
def mock_abort(code): raise Exception(f'Aborted with code: {code}') # pragma: no cover
abort = mock_abort # pragma: no cover
def mock_make_response(data): return data # pragma: no cover
make_response = mock_make_response # pragma: no cover
def mock_redirect(location): return f'Redirected to: {location}' # pragma: no cover
redirect = mock_redirect # pragma: no cover
def mock_render_template(template_name, **context): return f'Rendered template: {template_name} with context: {context}' # pragma: no cover
render_template = mock_render_template # pragma: no cover
def mock_request(): return type('MockRequest', (), {})() # pragma: no cover
request = mock_request() # pragma: no cover
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

