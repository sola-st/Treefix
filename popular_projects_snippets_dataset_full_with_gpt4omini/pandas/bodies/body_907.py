# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
df = DataFrame(
    index=range(3), columns=range(3), dtype=CategoricalDtype(["foo", "bar"])
)
df.at[1, 1] = "foo"

expected = DataFrame(
    [
        [np.nan, np.nan, np.nan],
        [np.nan, "foo", np.nan],
        [np.nan, np.nan, np.nan],
    ],
    dtype=CategoricalDtype(["foo", "bar"]),
)

tm.assert_frame_equal(df, expected)
