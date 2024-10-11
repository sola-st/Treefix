# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_ordered.py
result = merge_ordered(left, right, on="key")
expected = DataFrame(
    {
        "key": ["a", "b", "c", "d", "e", "f"],
        "lvalue": [1, np.nan, 2, np.nan, 3, np.nan],
        "rvalue": [np.nan, 1, 2, 3, np.nan, 4],
    }
)

tm.assert_frame_equal(result, expected)
