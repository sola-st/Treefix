import os # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

ctx = MagicMock() # pragma: no cover
param = MagicMock(name='param') # pragma: no cover
param.name = 'test_param' # pragma: no cover
ParameterSource = type('ParameterSource', (), {'DEFAULT': 'default', 'DEFAULT_MAP': 'default_map'}) # pragma: no cover
value = True # pragma: no cover
ctx.get_parameter_source = MagicMock(return_value=ParameterSource.DEFAULT) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
# If the flag isn't provided, it will default to False. Don't use
# that, let debug be set by env in that case.
from l3.Runtime import _l_
source = ctx.get_parameter_source(param.name)  # type: ignore[arg-type]
_l_(5281)  # type: ignore[arg-type]

if source is not None and source in (
    ParameterSource.DEFAULT,
    ParameterSource.DEFAULT_MAP,
):
    _l_(5283)

    aux = None
    _l_(5282)
    exit(aux)

# Set with env var instead of ScriptInfo.load so that it can be
# accessed early during a factory function.
os.environ["FLASK_DEBUG"] = "1" if value else "0"
_l_(5284)
aux = value
_l_(5285)
exit(aux)
