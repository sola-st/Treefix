# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# Merge on multiple columns
df3 = DataFrame({"col1": [0, 1], "col2": ["a", "b"]})

df4 = DataFrame({"col1": [1, 1, 3], "col2": ["b", "x", "y"]})

hand_coded_result = DataFrame(
    {"col1": [0, 1, 1, 3], "col2": ["a", "b", "x", "y"]}
)
hand_coded_result["_merge"] = Categorical(
    ["left_only", "both", "right_only", "right_only"],
    categories=["left_only", "right_only", "both"],
)

test5 = merge(df3, df4, on=["col1", "col2"], how="outer", indicator=True)
tm.assert_frame_equal(test5, hand_coded_result)
test5 = df3.merge(df4, on=["col1", "col2"], how="outer", indicator=True)
tm.assert_frame_equal(test5, hand_coded_result)
