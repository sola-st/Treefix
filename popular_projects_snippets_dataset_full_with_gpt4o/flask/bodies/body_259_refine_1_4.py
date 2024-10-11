import sys # pragma: no cover

value = 'app.module.path' # pragma: no cover
ctx = type('Mock', (object,), {'ensure_object': lambda self, x: x()})() # pragma: no cover
ScriptInfo = type('ScriptInfo', (object,), {}) # pragma: no cover

import sys # pragma: no cover

value = 'some_valid_value' # pragma: no cover
ctx = type('Mock', (object,), {'ensure_object': lambda self, x: x()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
if value is None:
    _l_(20764)

    aux = None
    _l_(20763)
    exit(aux)

info = ctx.ensure_object(ScriptInfo)
_l_(20765)
info.app_import_path = value
_l_(20766)
aux = value
_l_(20767)
exit(aux)
