from flask import Blueprint # pragma: no cover
from werkzeug.exceptions import HTTPException # pragma: no cover

class MockBlueprintSetupState: app = type('MockApp', (), {'jinja_env': type('MockJinjaEnv', (), {'tests': {}})()})() # pragma: no cover
self = type('MockSelf', (), {'record_once': lambda func: func})() # pragma: no cover
name = 'custom_test' # pragma: no cover
f = lambda x: x * 2 # pragma: no cover

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
