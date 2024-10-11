# Extracted from ./data/repos/flask/src/flask/wrappers.py
"""The endpoint that matched the request URL.

        This will be ``None`` if matching failed or has not been
        performed yet.

        This in combination with :attr:`view_args` can be used to
        reconstruct the same URL or a modified URL.
        """
if self.url_rule is not None:
    exit(self.url_rule.endpoint)

exit(None)
