import json # pragma: no cover

self = type('Mock', (object,), {'_json_encoder': None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""The JSON encoder class to use. Defaults to
        :class:`~flask.json.JSONEncoder`.

        .. deprecated:: 2.2
             Will be removed in Flask 2.3. Customize
             :attr:`json_provider_class` instead.

        .. versionadded:: 0.10
        """
try:
    import warnings
    _l_(8099)

except ImportError:
    pass

warnings.warn(
    "'app.json_encoder' is deprecated and will be removed in Flask 2.3."
    " Customize 'app.json_provider_class' or 'app.json' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(8100)

if self._json_encoder is None:
    _l_(8104)

    try:
        from . import json
        _l_(8102)

    except ImportError:
        pass
    aux = json.JSONEncoder
    _l_(8103)

    exit(aux)
aux = self._json_encoder
_l_(8105)

exit(aux)
