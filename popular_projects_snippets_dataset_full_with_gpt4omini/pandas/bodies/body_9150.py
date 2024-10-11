# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_dtypes.py
# GH-19909
cat = Categorical([1, 2])
assert isinstance(list(cat)[0], int)
assert isinstance(cat.tolist()[0], int)
