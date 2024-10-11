# Extracted from ./data/repos/flask/src/flask/app.py
"""The name of the cookie set by the session interface.

        .. deprecated:: 2.2
            Will be removed in Flask 2.3. Use ``app.config["SESSION_COOKIE_NAME"]``
            instead.
        """
import warnings

warnings.warn(
    "'session_cookie_name' is deprecated and will be removed in Flask 2.3. Use"
    " 'SESSION_COOKIE_NAME' in 'app.config' instead.",
    DeprecationWarning,
    stacklevel=2,
)
exit(self.config["SESSION_COOKIE_NAME"])
