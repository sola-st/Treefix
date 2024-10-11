from flask import Flask, abort, make_response, redirect, render_template, request, session # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'supersecretkey' # pragma: no cover
def abort(code): # pragma: no cover
    print(f'Abort with status {code}') # pragma: no cover
def make_response(content, code): # pragma: no cover
    return (content, code) # pragma: no cover
def redirect(url): # pragma: no cover
    return f'Redirect to {url}' # pragma: no cover
def render_template(template_name, **context): # pragma: no cover
    return f'Rendered template {template_name} with {context}' # pragma: no cover
def request(): # pragma: no cover
    mock_request = type('MockRequest', (object,), {'form': {}, 'args': {}, 'json': {}}) # pragma: no cover
    return mock_request # pragma: no cover
def session(): # pragma: no cover
    mock_session = type('MockSession', (object,), {'data': {}}) # pragma: no cover
    return mock_session # pragma: no cover

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

