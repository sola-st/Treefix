from types import SimpleNamespace # pragma: no cover

state = SimpleNamespace(app=SimpleNamespace(jinja_env=SimpleNamespace(filters={}))) # pragma: no cover
name = 'custom_filter' # pragma: no cover
def f(): return 'This is a custom filter' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
state.app.jinja_env.filters[name or f.__name__] = f
_l_(5568)
