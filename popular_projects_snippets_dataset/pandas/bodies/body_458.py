# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
cat = Categorical(categories)
assert cat.dtype._is_boolean is expected
assert is_bool_dtype(cat) is expected
assert is_bool_dtype(cat.dtype) is expected
