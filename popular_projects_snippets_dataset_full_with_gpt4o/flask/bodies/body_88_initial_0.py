self = type('Mock', (object,), {})() # pragma: no cover
value = 'json_decoder_value' # pragma: no cover
self._json_decoder = value # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(22626)

except ImportError:
    pass

warnings.warn(
    "'app.json_decoder' is deprecated and will be removed in Flask 2.3."
    " Customize 'app.json_provider_class' or 'app.json' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(22627)
self._json_decoder = value
_l_(22628)
