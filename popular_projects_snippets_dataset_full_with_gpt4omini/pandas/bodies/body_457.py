# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
categories = [(1, "a"), (2, "b"), (3, "c")]
result = CategoricalDtype(categories)
assert all(result.categories == categories)
