import warnings # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
value = None # pragma: no cover
self._json_decoder = value # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(9229)

except ImportError:
    pass

warnings.warn(
    "'bp.json_decoder' is deprecated and will be removed in Flask 2.3."
    " Customize 'app.json_provider_class' or 'app.json' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(9230)
self._json_decoder = value
_l_(9231)
