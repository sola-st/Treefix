from flask import Flask, Blueprint # pragma: no cover
from flask.blueprints import BlueprintSetupState # pragma: no cover

name = 'custom_global' # pragma: no cover
f = lambda: 'example_function' # pragma: no cover
self = type('Mock', (object,), {'record_once': lambda self, func: func})() # pragma: no cover

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
    _l_(22935)

    state.app.jinja_env.globals[name or f.__name__] = f
    _l_(22934)

self.record_once(register_template)
_l_(22936)
