class MockConfig:  # Mock configuration class# pragma: no cover
    def __init__(self):# pragma: no cover
        self.USE_X_SENDFILE = True  # Example value for demonstration# pragma: no cover
# pragma: no cover
self = type('Mock', (), {'config': MockConfig()})()  # Mock object with config attribute # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Enable this to use the ``X-Sendfile`` feature, assuming the server supports
        it, from :func:`~flask.send_file`.

        .. deprecated:: 2.2
            Will be removed in Flask 2.3. Use ``app.config["USE_X_SENDFILE"]`` instead.
        """
try:
    import warnings
    _l_(4067)

except ImportError:
    pass

warnings.warn(
    "'use_x_sendfile' is deprecated and will be removed in Flask 2.3. Use"
    " 'USE_X_SENDFILE' in 'app.config' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(4068)
aux = self.config["USE_X_SENDFILE"]
_l_(4069)
exit(aux)
