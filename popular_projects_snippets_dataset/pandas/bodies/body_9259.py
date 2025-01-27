# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH#49309 we should preserve orderedness in `res`
cat = Categorical([3, 1], categories=[3, 2, 1], ordered=True)

res = Categorical(cat, dtype="category")
assert res.dtype.ordered
