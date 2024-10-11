import json # pragma: no cover
from flask import Flask, current_app # pragma: no cover
import warnings # pragma: no cover
from decimal import Decimal # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
obj = {'key': 'value', 'number': Decimal('10.5')} # pragma: no cover
kwargs = {} # pragma: no cover
_default = str # pragma: no cover
_json = json # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/__init__.py
from l3.Runtime import _l_
"""Serialize data as JSON.

    If :data:`~flask.current_app` is available, it will use its
    :meth:`app.json.dumps() <flask.json.provider.JSONProvider.dumps>`
    method, otherwise it will use :func:`json.dumps`.

    :param obj: The data to serialize.
    :param kwargs: Arguments passed to the ``dumps`` implementation.

    .. versionchanged:: 2.2
        Calls ``current_app.json.dumps``, allowing an app to override
        the behavior.

    .. versionchanged:: 2.2
        The ``app`` parameter will be removed in Flask 2.3.

    .. versionchanged:: 2.0.2
        :class:`decimal.Decimal` is supported by converting to a string.

    .. versionchanged:: 2.0
        ``encoding`` will be removed in Flask 2.1.

    .. versionchanged:: 1.0.3
        ``app`` can be passed directly, rather than requiring an app
        context for configuration.
    """
if app is not None:
    _l_(5083)

    try:
        import warnings
        _l_(5080)

    except ImportError:
        pass

    warnings.warn(
        "The 'app' parameter is deprecated and will be removed in"
        " Flask 2.3. Call 'app.json.dumps' directly instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    _l_(5081)
else:
    app = current_app
    _l_(5082)

if app:
    _l_(5085)

    aux = app.json.dumps(obj, **kwargs)
    _l_(5084)
    exit(aux)

kwargs.setdefault("default", _default)
_l_(5086)
aux = _json.dumps(obj, **kwargs)
_l_(5087)
exit(aux)
