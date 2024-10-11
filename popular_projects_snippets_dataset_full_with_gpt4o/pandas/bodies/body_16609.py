# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH14887

left = pd.DataFrame({"a": [1, 5, 10], "left_val": ["a", "b", "c"]})
right = pd.DataFrame({"a": [1, 2, 3, 7, 11], "right_val": [1, 2, 3, 7, 11]})

expected = pd.DataFrame(
    {"a": [1, 5, 10], "left_val": ["a", "b", "c"], "right_val": [1, np.nan, 11]}
)

result = merge_asof(left, right, on="a", direction="nearest", tolerance=1)
tm.assert_frame_equal(result, expected)
