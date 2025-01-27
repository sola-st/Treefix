# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# assigning with a label that is in the categories but not in the index
df = df2.copy()
df.loc["e"] = 20
result = df.loc[["a", "b", "e"]]
exp_index = CategoricalIndex(list("aaabbe"), categories=list("cabe"), name="B")
expected = DataFrame({"A": [0, 1, 5, 2, 3, 20]}, index=exp_index)
tm.assert_frame_equal(result, expected)
