from flask import Flask, current_app # pragma: no cover
from flask.cli import ScriptInfo # pragma: no cover
from click import Context # pragma: no cover

current_app = None # pragma: no cover
ScriptInfo = type('ScriptInfo', (object,), {'load_app': lambda self: Flask(__name__)}) # pragma: no cover
f = lambda x: x # pragma: no cover
args = [] # pragma: no cover
kwargs = {} # pragma: no cover

from flask import Flask, current_app # pragma: no cover
from flask.cli import ScriptInfo # pragma: no cover
from click import Context # pragma: no cover

current_app = None # pragma: no cover
ScriptInfo = type('ScriptInfo', (object,), {'load_app': lambda self: Flask(__name__)}) # pragma: no cover
f = lambda *args: args # pragma: no cover
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
