# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# duplicated categories and codes
index = CategoricalIndex(["a", "b", "a"])
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=index)

# unique slice
res = df.loc[["a", "b"]]
exp = DataFrame(
    {"A": [1, 3, 2], "B": [4, 6, 5]}, index=CategoricalIndex(["a", "a", "b"])
)
tm.assert_frame_equal(res, exp, check_index_type=True)

# duplicated slice
res = df.loc[["a", "a", "b"]]
exp = DataFrame(
    {"A": [1, 3, 1, 3, 2], "B": [4, 6, 4, 6, 5]},
    index=CategoricalIndex(["a", "a", "a", "a", "b"]),
)
tm.assert_frame_equal(res, exp, check_index_type=True)

with pytest.raises(KeyError, match=re.escape("['x'] not in index")):
    df.loc[["a", "x"]]
