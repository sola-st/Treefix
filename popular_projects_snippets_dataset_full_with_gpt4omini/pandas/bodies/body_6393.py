# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
assert dtype == f"string[{dtype.storage}]"
super().test_eq_with_str(dtype)
