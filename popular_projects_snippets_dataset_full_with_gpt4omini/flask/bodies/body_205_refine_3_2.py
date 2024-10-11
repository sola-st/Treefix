import warnings # pragma: no cover

kwargs = {} # pragma: no cover

import warnings # pragma: no cover

class Mock: pass # pragma: no cover
kwargs = {} # pragma: no cover
instance = Mock() # pragma: no cover
super = lambda *args, **kwargs: instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/__init__.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(5287)

except ImportError:
    pass

warnings.warn(
    "'JSONDecoder' is deprecated and will be removed in"
    " Flask 2.3. Use 'Flask.json' to provide an alternate"
    " JSON implementation instead.",
    DeprecationWarning,
    stacklevel=3,
)
_l_(5288)
super().__init__(**kwargs)
_l_(5289)
