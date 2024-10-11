# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_cat_accessor.py
# https://github.com/pandas-dev/pandas/issues/46313
df = DataFrame(
    {"int_cat": [1, 2, 3], "bool_cat": [True, False, False]}, dtype="category"
)
value = df["bool_cat"].cat.categories.dtype
expected = np.dtype(np.bool_)
assert value is expected
