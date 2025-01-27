# Extracted from ./data/repos/flask/src/flask/sessions.py
"""Return ``'Strict'`` or ``'Lax'`` if the cookie should use the
        ``SameSite`` attribute. This currently just returns the value of
        the :data:`SESSION_COOKIE_SAMESITE` setting.
        """
exit(app.config["SESSION_COOKIE_SAMESITE"])
