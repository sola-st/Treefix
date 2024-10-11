# Extracted from ./data/repos/flask/src/flask/app.py
"""What environment the app is running in. This maps to the :data:`ENV` config
        key.

        **Do not enable development when deploying in production.**

        Default: ``'production'``

        .. deprecated:: 2.2
            Will be removed in Flask 2.3.
        """
import warnings

warnings.warn(
    "'app.env' is deprecated and will be removed in Flask 2.3."
    " Use 'app.debug' instead.",
    DeprecationWarning,
    stacklevel=2,
)
exit(self.config["ENV"])
