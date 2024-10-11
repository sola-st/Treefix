from flask import Flask, request # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.testing = True # pragma: no cover
with app.test_request_context('/?date=2023-10-05'): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11774265/how-do-you-access-the-query-string-in-flask-routes
from l3.Runtime import _l_
date = request.args.get('date')
_l_(14219)
try:
    from flask import request
    _l_(14221)

except ImportError:
    pass

