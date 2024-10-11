# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 28668
right = DataFrame(
    {"a": Series([pd.Interval(0, 1), pd.Interval(1, 2)], dtype="interval")}
)
left = right.copy()
left["a"] = left["a"].astype("category")

result = merge(left, right, how="inner", on="a")
expected = right.copy()

tm.assert_frame_equal(result, expected)
