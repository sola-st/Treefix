# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = Categorical([1, 2], categories=[1, 2, 3], ordered=True)
# override ordered
result = CategoricalDtype._from_categorical_dtype(c1, ordered=False)
assert result == CategoricalDtype([1, 2, 3], ordered=False)
