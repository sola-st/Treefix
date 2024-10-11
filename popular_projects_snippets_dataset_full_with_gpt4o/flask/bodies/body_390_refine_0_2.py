import warnings # pragma: no cover

name = '_app_ctx_stack' # pragma: no cover
__app_ctx_stack = 1 # pragma: no cover
__request_ctx_stack = 2 # pragma: no cover

import warnings # pragma: no cover
import sys # pragma: no cover

name = '_app_ctx_stack' # pragma: no cover
__app_ctx_stack = type('MockAppCtxStack', (object,), {})() # pragma: no cover
__request_ctx_stack = type('MockRequestCtxStack', (object,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/globals.py
from l3.Runtime import _l_
if name == "_app_ctx_stack":
    _l_(20082)

    try:
        import warnings
        _l_(20079)

    except ImportError:
        pass

    warnings.warn(
        "'_app_ctx_stack' is deprecated and will be removed in Flask 2.3.",
        DeprecationWarning,
        stacklevel=2,
    )
    _l_(20080)
    aux = __app_ctx_stack
    _l_(20081)
    exit(aux)

if name == "_request_ctx_stack":
    _l_(20087)

    try:
        import warnings
        _l_(20084)

    except ImportError:
        pass

    warnings.warn(
        "'_request_ctx_stack' is deprecated and will be removed in Flask 2.3.",
        DeprecationWarning,
        stacklevel=2,
    )
    _l_(20085)
    aux = __request_ctx_stack
    _l_(20086)
    exit(aux)

raise AttributeError(name)
_l_(20088)
