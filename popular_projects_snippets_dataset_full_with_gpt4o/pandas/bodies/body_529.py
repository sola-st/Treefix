# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = CategoricalDtype(categories, ordered)
result = c1 == other
expected = other == "category"
assert result is expected
