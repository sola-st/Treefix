from flask import current_app # pragma: no cover

_cv_app = type('Mock', (object,), {'get': lambda self, key: 'some_value' if key is None else None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Works like :func:`has_request_context` but for the application
    context.  You can also just do a boolean check on the
    :data:`current_app` object instead.

    .. versionadded:: 0.9
    """
aux = _cv_app.get(None) is not None
_l_(9227)
exit(aux)
