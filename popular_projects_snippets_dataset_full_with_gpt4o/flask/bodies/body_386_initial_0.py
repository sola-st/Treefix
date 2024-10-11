self = type('Mock', (object,), {'name': 'example_name'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/globals.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(22977)

except ImportError:
    pass

warnings.warn(
    f"'_{self.name}_ctx_stack' is deprecated and will be"
    " removed in Flask 2.3. Use 'g' to store data, or"
    f" '{self.name}_ctx' to access the current context.",
    DeprecationWarning,
    stacklevel=3,
)
_l_(22978)
