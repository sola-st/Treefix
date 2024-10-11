from flask import current_app, Flask, g # pragma: no cover
from flask.cli import ScriptInfo # pragma: no cover

current_app = None # pragma: no cover
__ctx = type('Mock', (object,), { 'ensure_object': lambda self, x: x(), 'with_resource': lambda self, x: None, 'invoke': lambda self, fn, *args, **kwargs: fn(*args, **kwargs) })() # pragma: no cover
ScriptInfo = type('Mock', (object,), { 'load_app': lambda self: type('App', (object,), { 'app_context': lambda self: 'mock_context' })() })() # pragma: no cover
f = lambda x: x + 1 # pragma: no cover
args = (1,) # pragma: no cover
kwargs = {'key': 'value'} # pragma: no cover

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
