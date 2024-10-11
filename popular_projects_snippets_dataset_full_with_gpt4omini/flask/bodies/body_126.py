# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Registers a function to be run before the first request to this
        instance of the application.

        The function will be called without any arguments and its return
        value is ignored.

        .. deprecated:: 2.2
            Will be removed in Flask 2.3. Run setup code when creating
            the application instead.

        .. versionadded:: 0.8
        """
try:
    import warnings
    _l_(9307)

except ImportError:
    pass

warnings.warn(
    "'before_first_request' is deprecated and will be removed"
    " in Flask 2.3. Run setup code while creating the"
    " application instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(9308)
self.before_first_request_funcs.append(f)
_l_(9309)
aux = f
_l_(9310)
exit(aux)
