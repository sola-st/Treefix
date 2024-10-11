# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#45369 filled columns should not be views of one another
df = DataFrame(index=[1, 2, 3], columns=["a", "b", "c"], copy=False)
assert not np.shares_memory(df["a"]._values, df["b"]._values)

df.iloc[0, 0] = 0
expected = DataFrame(
    {
        "a": [0, np.nan, np.nan],
        "b": [np.nan, np.nan, np.nan],
        "c": [np.nan, np.nan, np.nan],
    },
    index=[1, 2, 3],
    dtype=object,
)
tm.assert_frame_equal(df, expected)
