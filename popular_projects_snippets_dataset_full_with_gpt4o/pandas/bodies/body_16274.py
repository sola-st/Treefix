# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH12574
cat = Series(Categorical([1, 2, 3]), dtype="category")
assert is_categorical_dtype(cat)
assert is_categorical_dtype(cat.dtype)
