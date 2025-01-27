# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# though CategoricalDtype has object kind, it cannot be string
assert not is_string_dtype(CategoricalDtype())
