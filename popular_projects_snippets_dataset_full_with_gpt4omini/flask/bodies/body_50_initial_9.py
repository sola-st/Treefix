from flask import Blueprint # pragma: no cover
from flask import Flask # pragma: no cover

class Mock: pass # pragma: no cover
class BlueprintSetupState: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.app = Mock() # pragma: no cover
        self.app.jinja_env = Mock() # pragma: no cover
        self.app.jinja_env.tests = {} # pragma: no cover
self = Mock() # pragma: no cover
self.record_once = lambda fn: fn(BlueprintSetupState()) # pragma: no cover
name = 'custom_test' # pragma: no cover
f = lambda x: x  # Example test function # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Register a custom template test, available application wide.  Like
        :meth:`Flask.add_template_test` but for a blueprint.  Works exactly
        like the :meth:`app_template_test` decorator.

        .. versionadded:: 0.10

        :param name: the optional name of the test, otherwise the
                     function name will be used.
        """

def register_template(state: BlueprintSetupState) -> None:
    _l_(4821)

    state.app.jinja_env.tests[name or f.__name__] = f
    _l_(4820)

self.record_once(register_template)
_l_(4822)
