# Extracted from ./data/repos/flask/src/flask/blueprints.py
import warnings

warnings.warn(
    "'bp.json_encoder' is deprecated and will be removed in Flask 2.3."
    " Customize 'app.json_provider_class' or 'app.json' instead.",
    DeprecationWarning,
    stacklevel=2,
)
self._json_encoder = value
