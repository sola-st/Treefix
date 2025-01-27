# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# GH 11586

# unique categories and codes
index = CategoricalIndex(["a", "b", "c"])
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=index)

# unique slice
res = df.loc[["a", "b"]]
exp_index = CategoricalIndex(["a", "b"], categories=index.categories)
exp = DataFrame({"A": [1, 2], "B": [4, 5]}, index=exp_index)
tm.assert_frame_equal(res, exp, check_index_type=True)

# duplicated slice
res = df.loc[["a", "a", "b"]]

exp_index = CategoricalIndex(["a", "a", "b"], categories=index.categories)
exp = DataFrame({"A": [1, 1, 2], "B": [4, 4, 5]}, index=exp_index)
tm.assert_frame_equal(res, exp, check_index_type=True)

with pytest.raises(KeyError, match=re.escape("['x'] not in index")):
    df.loc[["a", "x"]]
