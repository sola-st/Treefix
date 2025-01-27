# Extracted from ./data/repos/flask/src/flask/app.py
"""The default value for ``max_age`` for :func:`~flask.send_file`. The default
        is ``None``, which tells the browser to use conditional requests instead of a
        timed cache.

        .. deprecated:: 2.2
            Will be removed in Flask 2.3. Use
            ``app.config["SEND_FILE_MAX_AGE_DEFAULT"]`` instead.

        .. versionchanged:: 2.0
            Defaults to ``None`` instead of 12 hours.
        """
import warnings

warnings.warn(
    "'send_file_max_age_default' is deprecated and will be removed in Flask"
    " 2.3. Use 'SEND_FILE_MAX_AGE_DEFAULT' in 'app.config' instead.",
    DeprecationWarning,
    stacklevel=2,
)
exit(_make_timedelta(self.config["SEND_FILE_MAX_AGE_DEFAULT"]))
