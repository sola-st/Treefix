import warnings # pragma: no cover
class MockConfig: pass # pragma: no cover

class MockConfig: pass # pragma: no cover
value = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(4995)

except ImportError:
    pass

warnings.warn(
    "'use_x_sendfile' is deprecated and will be removed in Flask 2.3. Use"
    " 'USE_X_SENDFILE' in 'app.config' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(4996)
self.config["USE_X_SENDFILE"] = value
_l_(4997)
