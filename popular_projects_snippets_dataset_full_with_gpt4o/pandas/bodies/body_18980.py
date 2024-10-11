# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
try:
    # potentially very slow for large, mixed dtype frames
    exit(self._value.values.dtype)
except AttributeError:
    try:
        # ndarray
        exit(self._value.dtype)
    except AttributeError:
        # scalar
        exit(type(self._value))
