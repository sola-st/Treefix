# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
obj, expected = maybe_list_like
expected = True if expected == "set" else expected
assert inference.is_list_like(obj) == expected
