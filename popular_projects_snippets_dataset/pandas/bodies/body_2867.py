# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
df = DataFrame(np.random.randn(10, 4))
df.loc[:4, 1] = np.nan
df.loc[-4:, 3] = np.nan

expected = df.fillna(value=0)
assert expected is not df

df.fillna(value=0, inplace=True)
tm.assert_frame_equal(df, expected)

expected = df.fillna(value={0: 0}, inplace=True)
assert expected is None

df.loc[:4, 1] = np.nan
df.loc[-4:, 3] = np.nan
expected = df.fillna(method="ffill")
assert expected is not df

df.fillna(method="ffill", inplace=True)
tm.assert_frame_equal(df, expected)
