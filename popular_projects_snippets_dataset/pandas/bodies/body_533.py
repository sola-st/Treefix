# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = Categorical([1, 2], categories=[1, 2, 3], ordered=True)
# override categories
result = CategoricalDtype._from_categorical_dtype(c1, categories=[2, 3])
assert result == CategoricalDtype([2, 3], ordered=True)
