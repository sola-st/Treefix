import json # pragma: no cover
from flask import Flask, current_app # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
fp = open('data.json', 'r') # pragma: no cover
kwargs = {} # pragma: no cover
_json = type('Mock', (object,), {'load': json.load}) # pragma: no cover
app.json = type('Mock', (object,), {'load': json.load}) # pragma: no cover

import json # pragma: no cover
import warnings # pragma: no cover
from flask import Flask # pragma: no cover

app = None # pragma: no cover
current_app = type('Mock', (object,), {'json': type('MockJSON', (object,), {'load': lambda f, *args, **kw: json.load(f)})()})() # pragma: no cover
with open('data.json', 'w') as f: f.write('{}') # pragma: no cover
fp = open('data.json', 'r') # pragma: no cover
kwargs = {} # pragma: no cover
_json = type('MockJSON', (object,), {'load': lambda f, *args, **kw: json.load(f)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/__init__.py
from l3.Runtime import _l_
"""Deserialize data as JSON read from a file.

    If :data:`~flask.current_app` is available, it will use its
    :meth:`app.json.load() <flask.json.provider.JSONProvider.load>`
    method, otherwise it will use :func:`json.load`.

    :param fp: A file opened for reading text or UTF-8 bytes.
    :param kwargs: Arguments passed to the ``load`` implementation.

    .. versionchanged:: 2.2
        Calls ``current_app.json.load``, allowing an app to override
        the behavior.

    .. versionchanged:: 2.2
        The ``app`` parameter will be removed in Flask 2.3.

    .. versionchanged:: 2.0
        ``encoding`` will be removed in Flask 2.1. The file must be text
        mode, or binary mode with UTF-8 bytes.
    """
if app is not None:
    _l_(22480)

    try:
        import warnings
        _l_(22477)

    except ImportError:
        pass

    warnings.warn(
        "The 'app' parameter is deprecated and will be removed in"
        " Flask 2.3. Call 'app.json.load' directly instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    _l_(22478)
else:
    app = current_app
    _l_(22479)

if app:
    _l_(22482)

    aux = app.json.load(fp, **kwargs)
    _l_(22481)
    exit(aux)
aux = _json.load(fp, **kwargs)
_l_(22483)

exit(aux)
