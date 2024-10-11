from flask import Blueprint # pragma: no cover

class MockApp: jinja_env = type('MockJinjaEnv', (object,), {'globals': {}})() # pragma: no cover
class MockBlueprintSetupState: app = MockApp() # pragma: no cover
state = MockBlueprintSetupState() # pragma: no cover
name = 'my_global_function' # pragma: no cover
f = lambda x: x * 2 # pragma: no cover

from flask import Flask, Blueprint # pragma: no cover

class MockJinjaEnv:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.globals = {}# pragma: no cover
# pragma: no cover
class MockApp:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.jinja_env = MockJinjaEnv()# pragma: no cover
# pragma: no cover
class MockBlueprintSetupState:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.app = MockApp() # pragma: no cover
state = MockBlueprintSetupState() # pragma: no cover
self = type('Mock', (), {'record_once': lambda self, func: func(state)})() # pragma: no cover
name = 'my_global_function' # pragma: no cover
f = lambda: 'Hello, World!' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Register a custom template global, available application wide.  Like
        :meth:`Flask.add_template_global` but for a blueprint.  Works exactly
        like the :meth:`app_template_global` decorator.

        .. versionadded:: 0.10

        :param name: the optional name of the global, otherwise the
                     function name will be used.
        """

def register_template(state: BlueprintSetupState) -> None:
    _l_(8957)

    state.app.jinja_env.globals[name or f.__name__] = f
    _l_(8956)

self.record_once(register_template)
_l_(8958)
