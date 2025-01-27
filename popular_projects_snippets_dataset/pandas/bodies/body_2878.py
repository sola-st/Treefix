# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH40989
df = DataFrame(
    [
        [np.nan, 2, np.nan, 0],
        [3, 4, np.nan, 1],
        [np.nan, np.nan, np.nan, 5],
        [np.nan, 3, np.nan, 4],
    ],
    columns=list("ABCD"),
)

expected = df.fillna(axis=1, value=100, limit=1)
assert expected is not df

df.fillna(axis=1, value=100, limit=1, inplace=True)
tm.assert_frame_equal(df, expected)
