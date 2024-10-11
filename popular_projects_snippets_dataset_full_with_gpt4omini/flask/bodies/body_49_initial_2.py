from jinja2 import Environment # pragma: no cover

state = type('MockState', (object,), {'app': type('MockApp', (object,), {'jinja_env': Environment()})()})() # pragma: no cover
name = 'test_function' # pragma: no cover
f = lambda x: x + 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
state.app.jinja_env.tests[name or f.__name__] = f
_l_(9222)
