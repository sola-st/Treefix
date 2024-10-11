from types import SimpleNamespace # pragma: no cover

state = SimpleNamespace(app=SimpleNamespace(jinja_env=SimpleNamespace(filters={}))) # pragma: no cover
name = 'example_filter' # pragma: no cover
f = type('MockFunction', (object,), {'__name__': 'mock_function'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
state.app.jinja_env.filters[name or f.__name__] = f
_l_(17292)
