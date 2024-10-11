from flask import Flask, current_app, g # pragma: no cover

class Mock: pass # pragma: no cover
__ctx = Mock() # pragma: no cover
def ensure_object(self, obj): return obj # pragma: no cover
def with_resource(self, resource): pass # pragma: no cover
def invoke(self, f, *args, **kwargs): return f(*args, **kwargs) # pragma: no cover
__ctx.ensure_object = ensure_object.__get__(__ctx) # pragma: no cover
__ctx.with_resource = with_resource.__get__(__ctx) # pragma: no cover
__ctx.invoke = invoke.__get__(__ctx) # pragma: no cover
class ScriptInfo: pass # pragma: no cover
f = lambda x: x * 2 # pragma: no cover
args = (5,) # pragma: no cover
kwargs = {} # pragma: no cover

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
