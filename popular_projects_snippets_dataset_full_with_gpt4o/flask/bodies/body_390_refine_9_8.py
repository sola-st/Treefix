import sys # pragma: no cover

name = '_app_ctx_stack' # pragma: no cover

import sys # pragma: no cover

name = '_app_ctx_stack' # pragma: no cover
__app_ctx_stack = 0 # pragma: no cover
__request_ctx_stack = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/globals.py
from l3.Runtime import _l_
if name == "_app_ctx_stack":
    _l_(20041)

    try:
        import warnings
        _l_(20038)

    except ImportError:
        pass

    warnings.warn(
        "'_app_ctx_stack' is deprecated and will be removed in Flask 2.3.",
        DeprecationWarning,
        stacklevel=2,
    )
    _l_(20039)
    aux = __app_ctx_stack
    _l_(20040)
    exit(aux)

if name == "_request_ctx_stack":
    _l_(20046)

    try:
        import warnings
        _l_(20043)

    except ImportError:
        pass

    warnings.warn(
        "'_request_ctx_stack' is deprecated and will be removed in Flask 2.3.",
        DeprecationWarning,
        stacklevel=2,
    )
    _l_(20044)
    aux = __request_ctx_stack
    _l_(20045)
    exit(aux)

raise AttributeError(name)
_l_(20047)
