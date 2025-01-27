# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
left_df = DataFrame({"A": [100, 200, 1], "B": [60, 70, 80]})
right_df = DataFrame({"A": [100, 200, 300], "B": [600, 700, 800]})
result = merge(left_df, right_df, on="A", how=how, suffixes=("_x", "_x"))
expected.columns = ["A", "B_x", "B_x"]

tm.assert_frame_equal(result, expected)
