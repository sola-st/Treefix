# Extracted from ./data/repos/flask/src/flask/app.py
"""Returns the value of the ``PROPAGATE_EXCEPTIONS`` configuration
        value in case it's set, otherwise a sensible default is returned.

        .. deprecated:: 2.2
            Will be removed in Flask 2.3.

        .. versionadded:: 0.7
        """
import warnings

warnings.warn(
    "'propagate_exceptions' is deprecated and will be removed in Flask 2.3.",
    DeprecationWarning,
    stacklevel=2,
)
rv = self.config["PROPAGATE_EXCEPTIONS"]
if rv is not None:
    exit(rv)
exit(self.testing or self.debug)
