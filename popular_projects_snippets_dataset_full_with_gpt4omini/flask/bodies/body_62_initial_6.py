from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {'record_once': lambda f: f()})() # pragma: no cover
f = lambda s: s + '_processed' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Same as :meth:`url_value_preprocessor` but application wide."""
self.record_once(
    lambda s: s.app.url_value_preprocessors.setdefault(None, []).append(f)
)
_l_(8364)
aux = f
_l_(8365)
exit(aux)
