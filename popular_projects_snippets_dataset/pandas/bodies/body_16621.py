# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH14887

left = pd.DataFrame(
    {
        "a": [1, 5, 10, 12, 15],
        "b": ["X", "X", "Y", "Z", "Y"],
        "left_val": ["a", "b", "c", "d", "e"],
    }
)
right = pd.DataFrame(
    {
        "a": [1, 6, 11, 15, 16],
        "b": ["X", "Z", "Y", "Z", "Y"],
        "right_val": [1, 6, 11, 15, 16],
    }
)

expected = pd.DataFrame(
    {
        "a": [1, 5, 10, 12, 15],
        "b": ["X", "X", "Y", "Z", "Y"],
        "left_val": ["a", "b", "c", "d", "e"],
        "right_val": [1, np.nan, 11, 15, 16],
    }
)

result = merge_asof(left, right, on="a", by="b", direction="forward")
tm.assert_frame_equal(result, expected)
