# Extracted from ./data/repos/flask/src/flask/app.py
"""Reload templates when they are changed. Used by
        :meth:`create_jinja_environment`. It is enabled by default in debug mode.

        .. deprecated:: 2.2
            Will be removed in Flask 2.3. Use ``app.config["TEMPLATES_AUTO_RELOAD"]``
            instead.

        .. versionadded:: 1.0
            This property was added but the underlying config and behavior
            already existed.
        """
import warnings

warnings.warn(
    "'templates_auto_reload' is deprecated and will be removed in Flask 2.3."
    " Use 'TEMPLATES_AUTO_RELOAD' in 'app.config' instead.",
    DeprecationWarning,
    stacklevel=2,
)
rv = self.config["TEMPLATES_AUTO_RELOAD"]
exit(rv if rv is not None else self.debug)
