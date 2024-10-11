# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# GH39881
df1 = DataFrame(
    {"x": [9, 10, 11]},
    index=MultiIndex.from_arrays([[1, 2, 3], [np.nan, 5, 6]], names=["a", "b"]),
)

df2 = DataFrame(
    {"y": [12, 13, 14]},
    index=MultiIndex.from_arrays([[1, 2, 4], [np.nan, 5, 7]], names=["a", "b"]),
)

expected = DataFrame(
    {
        "x": [9.0, 10.0, 11.0, np.nan],
        "y": [12.0, 13.0, np.nan, 14.0],
    },
    index=MultiIndex.from_arrays(
        [[1, 2, 3, 4], [np.nan, 5.0, 6.0, 7.0]], names=["a", "b"]
    ),
)
combined = df1.combine_first(df2)
tm.assert_frame_equal(combined, expected)
