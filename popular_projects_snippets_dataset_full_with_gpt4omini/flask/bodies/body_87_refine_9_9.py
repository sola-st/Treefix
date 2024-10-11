from flask import Flask # pragma: no cover
import json # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {'_json_decoder': None})() # pragma: no cover

import json # pragma: no cover
import warnings # pragma: no cover

self = type('Mock', (object,), {'_json_decoder': None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""The JSON decoder class to use. Defaults to
        :class:`~flask.json.JSONDecoder`.

        .. deprecated:: 2.2
             Will be removed in Flask 2.3. Customize
             :attr:`json_provider_class` instead.

        .. versionadded:: 0.10
        """
try:
    import warnings
    _l_(3883)

except ImportError:
    pass

warnings.warn(
    "'app.json_decoder' is deprecated and will be removed in Flask 2.3."
    " Customize 'app.json_provider_class' or 'app.json' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(3884)

if self._json_decoder is None:
    _l_(3888)

    try:
        from . import json
        _l_(3886)

    except ImportError:
        pass
    aux = json.JSONDecoder
    _l_(3887)

    exit(aux)
aux = self._json_decoder
_l_(3889)

exit(aux)
