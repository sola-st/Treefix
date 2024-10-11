from types import SimpleNamespace # pragma: no cover

state = SimpleNamespace(app=SimpleNamespace(jinja_env=SimpleNamespace(globals={}))) # pragma: no cover
name = None # pragma: no cover
f = type('Mock', (object,), {'__name__': 'example_function'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
state.app.jinja_env.globals[name or f.__name__] = f
_l_(18141)
