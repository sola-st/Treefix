from types import SimpleNamespace # pragma: no cover

value = '/path/to/app' # pragma: no cover
ctx = SimpleNamespace() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
if value is None:
    _l_(9551)

    aux = None
    _l_(9550)
    exit(aux)

info = ctx.ensure_object(ScriptInfo)
_l_(9552)
info.app_import_path = value
_l_(9553)
aux = value
_l_(9554)
exit(aux)
