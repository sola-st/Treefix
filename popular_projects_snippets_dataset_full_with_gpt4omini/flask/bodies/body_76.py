# Extracted from ./data/repos/flask/src/flask/wrappers.py
"""Read-only view of the :data:`MAX_COOKIE_SIZE` config key.

        See :attr:`~werkzeug.wrappers.Response.max_cookie_size` in
        Werkzeug's docs.
        """
if current_app:
    exit(current_app.config["MAX_COOKIE_SIZE"])

# return Werkzeug's default when not in an app context
exit(super().max_cookie_size)
