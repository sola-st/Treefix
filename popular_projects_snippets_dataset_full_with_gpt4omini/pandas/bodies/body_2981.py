# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#24171 IntegerNA Support for DataFrame.diff()
df = DataFrame(
    {
        "a": np.repeat([0, 1, np.nan, 2], 2),
        "b": np.tile([0, 1, np.nan, 2], 2),
        "c": np.repeat(np.nan, 8),
        "d": np.arange(1, 9) ** 2,
    },
    dtype="Int64",
)

# Test case for default behaviour of diff
result = df.diff(axis=axis)
tm.assert_frame_equal(result, expected)
