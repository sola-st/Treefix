# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(22938)

except ImportError:
    pass

warnings.warn(
    "'app.json_encoder' is deprecated and will be removed in Flask 2.3."
    " Customize 'app.json_provider_class' or 'app.json' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(22939)
self._json_encoder = value
_l_(22940)
