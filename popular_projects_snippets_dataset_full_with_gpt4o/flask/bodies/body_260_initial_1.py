import os # pragma: no cover

ctx = type('MockCtx', (object,), {'get_parameter_source': lambda self, name: 'ParameterSource.DEFAULT'})() # pragma: no cover
param = type('MockParam', (object,), {'name': 'param_name'})() # pragma: no cover
ParameterSource = type('ParameterSource', (object,), {'DEFAULT': 'ParameterSource.DEFAULT', 'DEFAULT_MAP': 'ParameterSource.DEFAULT_MAP'}) # pragma: no cover
value = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
# If the flag isn't provided, it will default to False. Don't use
# that, let debug be set by env in that case.
from l3.Runtime import _l_
source = ctx.get_parameter_source(param.name)  # type: ignore[arg-type]
_l_(22584)  # type: ignore[arg-type]

if source is not None and source in (
    ParameterSource.DEFAULT,
    ParameterSource.DEFAULT_MAP,
):
    _l_(22586)

    aux = None
    _l_(22585)
    exit(aux)

# Set with env var instead of ScriptInfo.load so that it can be
# accessed early during a factory function.
os.environ["FLASK_DEBUG"] = "1" if value else "0"
_l_(22587)
aux = value
_l_(22588)
exit(aux)
