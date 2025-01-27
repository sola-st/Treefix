# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH#43550
left = DataFrame({"key": [1, 2], "col1": [1, 2]}, dtype=dtype)
right = DataFrame({"key": [np.nan, np.nan], "col2": [3, 4]}, dtype=dtype)
result = merge(left, right, on="key", how="outer")
expected = DataFrame(
    {
        "key": [1, 2, np.nan, np.nan],
        "col1": [1, 2, np.nan, np.nan],
        "col2": [np.nan, np.nan, 3, 4],
    },
    dtype=dtype,
)
tm.assert_frame_equal(result, expected)

# switch left and right
result = merge(right, left, on="key", how="outer")
expected = DataFrame(
    {
        "key": [np.nan, np.nan, 1, 2],
        "col2": [3, 4, np.nan, np.nan],
        "col1": [np.nan, np.nan, 1, 2],
    },
    dtype=dtype,
)
tm.assert_frame_equal(result, expected)
