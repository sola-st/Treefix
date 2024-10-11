# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame(
    {
        0: {35: np.nan, 40: np.nan, 43: np.nan, 49: np.nan, 50: np.nan},
        1: {
            35: np.nan,
            40: 0.32632316859446198,
            43: np.nan,
            49: 0.32632316859446198,
            50: 0.39114724480578139,
        },
        2: {
            35: np.nan,
            40: np.nan,
            43: 0.29012581014105987,
            49: np.nan,
            50: np.nan,
        },
        3: {35: np.nan, 40: np.nan, 43: np.nan, 49: np.nan, 50: np.nan},
        4: {
            35: 0.34215328467153283,
            40: np.nan,
            43: np.nan,
            49: np.nan,
            50: np.nan,
        },
        "y": {35: 0, 40: 0, 43: 0, 49: 0, 50: 1},
    }
)

# mixed int/float ok
df2 = df.copy()
df2[df2 > 0.3] = 1
expected = df.copy()
expected.loc[40, 1] = 1
expected.loc[49, 1] = 1
expected.loc[50, 1] = 1
expected.loc[35, 4] = 1
tm.assert_frame_equal(df2, expected)

df["foo"] = "test"
msg = "not supported between instances|unorderable types"

with pytest.raises(TypeError, match=msg):
    df[df > 0.3] = 1
