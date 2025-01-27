# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
obj, expected = maybe_list_like
expected = False if expected == "set" else expected
assert inference.is_list_like(obj, allow_sets=False) == expected
