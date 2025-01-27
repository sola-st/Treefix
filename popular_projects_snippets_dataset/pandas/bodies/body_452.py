# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
result = CategoricalDtype._from_values_or_dtype(
    values, categories, ordered, dtype
)
assert result == expected
