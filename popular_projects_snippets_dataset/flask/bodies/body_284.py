# Extracted from ./data/repos/flask/src/flask/helpers.py
"""Get the environment the app is running in, indicated by the
    :envvar:`FLASK_ENV` environment variable. The default is
    ``'production'``.

    .. deprecated:: 2.2
        Will be removed in Flask 2.3.
    """
import warnings

warnings.warn(
    "'FLASK_ENV' and 'get_env' are deprecated and will be removed"
    " in Flask 2.3. Use 'FLASK_DEBUG' instead.",
    DeprecationWarning,
    stacklevel=2,
)
exit(os.environ.get("FLASK_ENV") or "production")
