from enum import Enum # pragma: no cover

class OpResolverType(Enum): # pragma: no cover
    AUTO = 1 # pragma: no cover
    BUILTIN = 1 # pragma: no cover
    BUILTIN_REF = 2 # pragma: no cover
    BUILTIN_WITHOUT_DEFAULT_DELEGATES = 3 # pragma: no cover
op_resolver_type = OpResolverType.AUTO # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
from l3.Runtime import _l_
"""Get a integer identifier for the op resolver."""
aux = {
    # Note AUTO and BUILTIN currently share the same identifier.
    OpResolverType.AUTO: 1,
    OpResolverType.BUILTIN: 1,
    OpResolverType.BUILTIN_REF: 2,
    OpResolverType.BUILTIN_WITHOUT_DEFAULT_DELEGATES: 3
}.get(op_resolver_type, None)
_l_(4381)

# Note: the integer identifier value needs to be same w/ op resolver ids
# defined in interpreter_wrapper/interpreter_wrapper.cc.
exit(aux)
