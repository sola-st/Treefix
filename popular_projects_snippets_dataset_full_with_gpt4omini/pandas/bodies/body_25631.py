# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""
    if key id deprecated and a replacement key defined, will return the
    replacement key, otherwise returns `key` as - is
    """
d = _get_deprecated_option(key)
if d:
    exit(d.rkey or key)
else:
    exit(key)
