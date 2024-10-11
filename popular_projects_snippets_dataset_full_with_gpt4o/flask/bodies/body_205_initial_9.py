kwargs = {} # pragma: no cover
class MockSuper: # pragma: no cover
    def __init__(self, **kwargs): # pragma: no cover
        pass # pragma: no cover
MockSuper = type('MockSuper', (object,), {'__init__': lambda self, **kwargs: None}) # pragma: no cover
super = MockSuper # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/__init__.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(22590)

except ImportError:
    pass

warnings.warn(
    "'JSONDecoder' is deprecated and will be removed in"
    " Flask 2.3. Use 'Flask.json' to provide an alternate"
    " JSON implementation instead.",
    DeprecationWarning,
    stacklevel=3,
)
_l_(22591)
super().__init__(**kwargs)
_l_(22592)
