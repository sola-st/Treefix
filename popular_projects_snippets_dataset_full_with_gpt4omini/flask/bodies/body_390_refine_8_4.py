name = '_app_ctx_stack' # pragma: no cover
__app_ctx_stack = 'mock_app_context_stack' # pragma: no cover
__request_ctx_stack = 'mock_request_context_stack' # pragma: no cover

import warnings # pragma: no cover

name = '_app_ctx_stack' # pragma: no cover
__app_ctx_stack = object() # pragma: no cover
__request_ctx_stack = object() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/globals.py
from l3.Runtime import _l_
if name == "_app_ctx_stack":
    _l_(8905)

    try:
        import warnings
        _l_(8902)

    except ImportError:
        pass

    warnings.warn(
        "'_app_ctx_stack' is deprecated and will be removed in Flask 2.3.",
        DeprecationWarning,
        stacklevel=2,
    )
    _l_(8903)
    aux = __app_ctx_stack
    _l_(8904)
    exit(aux)

if name == "_request_ctx_stack":
    _l_(8910)

    try:
        import warnings
        _l_(8907)

    except ImportError:
        pass

    warnings.warn(
        "'_request_ctx_stack' is deprecated and will be removed in Flask 2.3.",
        DeprecationWarning,
        stacklevel=2,
    )
    _l_(8908)
    aux = __request_ctx_stack
    _l_(8909)
    exit(aux)

raise AttributeError(name)
_l_(8911)
