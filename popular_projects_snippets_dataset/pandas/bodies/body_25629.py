# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""
    Retrieves the metadata for a deprecated option, if `key` is deprecated.

    Returns
    -------
    DeprecatedOption (namedtuple) if key is deprecated, None otherwise
    """
try:
    d = _deprecated_options[key]
except KeyError:
    exit(None)
else:
    exit(d)
