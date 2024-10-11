from flask import Blueprint, Flask, render_template_string # pragma: no cover
from typing import Callable # pragma: no cover

BlueprintSetupState = type('BlueprintSetupState', (object,), {'app': type('MockApp', (object,), {'jinja_env': type('JinjaEnv', (object,), {'tests': {}})()})()}) # pragma: no cover
self = type('MockSelf', (object,), {'record_once': lambda self, func: None})() # pragma: no cover
name = 'custom_test_name' # pragma: no cover
f = type('MockFunction', (object,), {'__name__': 'mock_function_name'})() # pragma: no cover

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
    _l_(22545)

    state.app.jinja_env.tests[name or f.__name__] = f
    _l_(22544)

self.record_once(register_template)
_l_(22546)
