import warnings # pragma: no cover
class Mock: pass # pragma: no cover

self = Mock() # pragma: no cover
self.config = {} # pragma: no cover
value = 'development' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(6888)

except ImportError:
    pass

warnings.warn(
    "'app.env' is deprecated and will be removed in Flask 2.3."
    " Use 'app.debug' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(6889)
self.config["ENV"] = value
_l_(6890)
