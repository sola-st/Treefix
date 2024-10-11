from types import FunctionType # pragma: no cover

class MockApp: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.jinja_env = type('MockJinjaEnv', (object,), {'globals': {}})() # pragma: no cover
state = type('Mock', (object,), {'app': MockApp()})() # pragma: no cover
name = 'my_function' # pragma: no cover
def f(): return 'Hello, World!' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
state.app.jinja_env.globals[name or f.__name__] = f
_l_(6886)
