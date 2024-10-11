import warnings # pragma: no cover
from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {'config': {}})() # pragma: no cover
value = 'my_session_cookie' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(5258)

except ImportError:
    pass

warnings.warn(
    "'session_cookie_name' is deprecated and will be removed in Flask 2.3. Use"
    " 'SESSION_COOKIE_NAME' in 'app.config' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(5259)
self.config["SESSION_COOKIE_NAME"] = value
_l_(5260)
