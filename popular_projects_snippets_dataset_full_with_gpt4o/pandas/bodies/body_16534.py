# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# https://github.com/pandas-dev/pandas/issues/37465
g = np.random.RandomState(25982704)
a = Series(g.randint(0, 3, size=100)).astype(a_dtype)
b = Series(g.randint(0, 2, size=100)).astype(b_dtype)
result = crosstab(a, b, margins=True, dropna=False)
columns = Index([0, 1, "All"], dtype="object", name="col_0")
index = Index([0, 1, 2, "All"], dtype="object", name="row_0")
values = [[18, 16, 34], [18, 16, 34], [16, 16, 32], [52, 48, 100]]
expected = DataFrame(values, index, columns)
tm.assert_frame_equal(result, expected)

# Verify when categorical does not have all values present
a.loc[a == 1] = 2
a_is_cat = is_categorical_dtype(a.dtype)
assert not a_is_cat or a.value_counts().loc[1] == 0
result = crosstab(a, b, margins=True, dropna=False)
values = [[18, 16, 34], [0, 0, 0], [34, 32, 66], [52, 48, 100]]
expected = DataFrame(values, index, columns)
if not a_is_cat:
    expected = expected.loc[[0, 2, "All"]]
    expected["All"] = expected["All"].astype("int64")
repr(result)
repr(expected)
repr(expected.loc[[0, 2, "All"]])
tm.assert_frame_equal(result, expected)
