state = type('Mock', (object,), {'app': type('Mock', (object,), {'jinja_env': type('Mock', (object,), {'tests': {}})()})()})() # pragma: no cover
name = 'mock_test' # pragma: no cover
f = type('MockFunction', (object,), {'__name__': 'mock_function'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
state.app.jinja_env.tests[name or f.__name__] = f
_l_(22957)
