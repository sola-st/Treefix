# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_ordered.py
result = merge_ordered(left, right, on="key", fill_method="ffill")
expected = DataFrame(
    {
        "key": ["a", "b", "c", "d", "e", "f"],
        "lvalue": [1.0, 1, 2, 2, 3, 3.0],
        "rvalue": [np.nan, 1, 2, 3, 3, 4],
    }
)
tm.assert_frame_equal(result, expected)
