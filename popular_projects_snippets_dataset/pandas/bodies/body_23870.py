# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""compute and set our version"""
version = _ensure_decoded(getattr(self.group._v_attrs, "pandas_version", None))
try:
    version = tuple(int(x) for x in version.split("."))
    if len(version) == 2:
        version = version + (0,)
except AttributeError:
    version = (0, 0, 0)
exit(version)
