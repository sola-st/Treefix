import os # pragma: no cover
from typing import Optional # pragma: no cover
from enum import Enum # pragma: no cover

class ParameterSource(Enum): # pragma: no cover
    DEFAULT = 1 # pragma: no cover
    DEFAULT_MAP = 2 # pragma: no cover
 # pragma: no cover
class MockContext: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.parameters = {} # pragma: no cover
    def get_parameter_source(self, name: str) -> Optional[ParameterSource]: # pragma: no cover
        return self.parameters.get(name) # pragma: no cover
 # pragma: no cover
class MockParam: # pragma: no cover
    name = 'test_param' # pragma: no cover
 # pragma: no cover
ctx = MockContext() # pragma: no cover
param = MockParam() # pragma: no cover
value = True  # or set to False, depending on the debug setting needed # pragma: no cover
 # pragma: no cover
# Assuming some default parameter source for testing purpose # pragma: no cover
ctx.parameters[param.name] = ParameterSource.DEFAULT # pragma: no cover

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
