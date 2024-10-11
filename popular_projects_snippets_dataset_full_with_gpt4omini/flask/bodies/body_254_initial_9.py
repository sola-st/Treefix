from flask import Flask, current_app # pragma: no cover
from unittest.mock import Mock # pragma: no cover

current_app = None # pragma: no cover
__ctx = Mock() # pragma: no cover
ScriptInfo = type('ScriptInfo', (object,), {'load_app': lambda self: Mock(app_context=Mock())}) # pragma: no cover
f = Mock() # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover
__ctx.ensure_object = lambda x: x # pragma: no cover
__ctx.with_resource = lambda x: None # pragma: no cover
__ctx.invoke = lambda f, *args, **kwargs: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
if not current_app:
    _l_(8658)

    app = __ctx.ensure_object(ScriptInfo).load_app()
    _l_(8656)
    __ctx.with_resource(app.app_context())
    _l_(8657)
aux = __ctx.invoke(f, *args, **kwargs)
_l_(8659)

exit(aux)
