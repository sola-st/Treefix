from flask import Flask, current_app # pragma: no cover
from flask.cli import ScriptInfo # pragma: no cover

class Mock(object): pass # pragma: no cover
__ctx = Mock() # pragma: no cover
__ctx.ensure_object = lambda cls: cls() # pragma: no cover
__ctx.with_resource = lambda ctx: ctx.push() # pragma: no cover
__ctx.invoke = lambda f, *args, **kwargs: f(*args, **kwargs) # pragma: no cover
class AppContext(object): # pragma: no cover
    def push(self): pass # pragma: no cover
class App(object): # pragma: no cover
    def app_context(self): return AppContext() # pragma: no cover
__ctx.ensure_object = lambda cls: type('ScriptInfoMock', (cls,), {'load_app': lambda self: App()})() # pragma: no cover
f = lambda *args, **kwargs: 'Function executed' # pragma: no cover
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
