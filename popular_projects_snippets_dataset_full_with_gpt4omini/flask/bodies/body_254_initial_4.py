from click import Command, Context as ClickContext # pragma: no cover

current_app = None # pragma: no cover
__ctx = ClickContext(command=Command(name='dummy_command'), parent=None) # pragma: no cover
class ScriptInfo: # pragma: no cover
    def load_app(self): # pragma: no cover
        app = Flask(__name__) # pragma: no cover
        return app # pragma: no cover
ScriptInfo = ScriptInfo() # pragma: no cover
f = Command(name='dummy_command') # pragma: no cover
args = [] # pragma: no cover
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
