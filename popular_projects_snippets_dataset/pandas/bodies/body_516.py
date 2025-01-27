# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH30568: though IntervalDtype has object kind, it cannot be string
assert not is_string_dtype(IntervalDtype())
