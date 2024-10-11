from flask import Flask, current_app # pragma: no cover
from flask.cli import ScriptInfo # pragma: no cover

current_app = None # pragma: no cover
__ctx = type('Mock', (object,), { # pragma: no cover
    'ensure_object': lambda self, cls: ScriptInfo(), # pragma: no cover
    'with_resource': lambda self, ctx: ctx.__enter__(), # pragma: no cover
    'invoke': lambda self, f, *args, **kwargs: f(*args, **kwargs) # pragma: no cover
})() # pragma: no cover
ScriptInfo = ScriptInfo # pragma: no cover
f = lambda *args, **kwargs: 'Function executed successfully' # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
if not current_app:
    _l_(22901)

    app = __ctx.ensure_object(ScriptInfo).load_app()
    _l_(22899)
    __ctx.with_resource(app.app_context())
    _l_(22900)
aux = __ctx.invoke(f, *args, **kwargs)
_l_(22902)

exit(aux)
