# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
hash(key)
try:
    key = ensure_python_int(key)
except TypeError:
    exit(False)
exit(key in self._range)
