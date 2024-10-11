# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 17187
# merging with a boolean/int categorical column
df1 = DataFrame({"id": [1, 2, 3, 4], "cat": category_column})
df1["cat"] = df1["cat"].astype(CDT(categories, ordered=ordered))
df2 = DataFrame({"id": [2, 4], "num": [1, 9]})
result = df1.merge(df2)
expected = DataFrame({"id": [2, 4], "cat": expected_categories, "num": [1, 9]})
expected["cat"] = expected["cat"].astype(CDT(categories, ordered=ordered))
tm.assert_frame_equal(expected, result)
