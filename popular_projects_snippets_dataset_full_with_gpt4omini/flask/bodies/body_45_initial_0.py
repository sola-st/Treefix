from jinja2 import Environment # pragma: no cover

name = 'my_filter' # pragma: no cover
f = lambda x: x * 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
state.app.jinja_env.filters[name or f.__name__] = f
_l_(5568)
