# Extracted from ./data/repos/flask/src/flask/app.py
"""Create a redirect response object.

        This is called by :func:`flask.redirect`, and can be called
        directly as well.

        :param location: The URL to redirect to.
        :param code: The status code for the redirect.

        .. versionadded:: 2.2
            Moved from ``flask.redirect``, which calls this method.
        """
exit(_wz_redirect(location, code=code, Response=self.response_class))
