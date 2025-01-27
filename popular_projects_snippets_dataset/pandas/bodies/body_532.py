# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = Categorical([1, 2], categories=[1, 2, 3], ordered=True)
# Identity test for no changes
c2 = CategoricalDtype._from_categorical_dtype(c1)
assert c2 is c1
