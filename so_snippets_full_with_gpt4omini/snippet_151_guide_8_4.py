from flask import Flask, abort, make_response, redirect, render_template, request, session # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'dummy_secret_key' # pragma: no cover
abort = lambda code: f'Aborted with code: {code}' # pragma: no cover
make_response = lambda response_data: f'Response created with: {response_data}' # pragma: no cover
redirect = lambda url: f'Redirected to: {url}' # pragma: no cover
render_template = lambda template_name, **context: f'Rendered {template_name} with context: {context}' # pragma: no cover
request = type('MockRequest', (object,), {'args': {'key': 'value'}})() # pragma: no cover
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

