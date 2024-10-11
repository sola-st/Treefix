# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
try:
    import warnings
    _l_(7705)

except ImportError:
    pass

warnings.warn(
    "'templates_auto_reload' is deprecated and will be removed in Flask 2.3."
    " Use 'TEMPLATES_AUTO_RELOAD' in 'app.config' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(7706)
self.config["TEMPLATES_AUTO_RELOAD"] = value
_l_(7707)
