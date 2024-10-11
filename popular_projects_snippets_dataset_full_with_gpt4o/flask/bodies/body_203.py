# Extracted from ./data/repos/flask/src/flask/json/__init__.py
import warnings

warnings.warn(
    "'JSONEncoder' is deprecated and will be removed in"
    " Flask 2.3. Use 'Flask.json' to provide an alternate"
    " JSON implementation instead.",
    DeprecationWarning,
    stacklevel=3,
)
super().__init__(**kwargs)
