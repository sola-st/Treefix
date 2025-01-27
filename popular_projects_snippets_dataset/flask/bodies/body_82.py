# Extracted from ./data/repos/flask/src/flask/app.py
import warnings

warnings.warn(
    "'send_file_max_age_default' is deprecated and will be removed in Flask"
    " 2.3. Use 'SEND_FILE_MAX_AGE_DEFAULT' in 'app.config' instead.",
    DeprecationWarning,
    stacklevel=2,
)
self.config["SEND_FILE_MAX_AGE_DEFAULT"] = _make_timedelta(value)
