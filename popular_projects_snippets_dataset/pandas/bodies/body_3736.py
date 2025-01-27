# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
df = DataFrame(np.random.randn(6, 4))
df.iloc[:2, 2] = np.nan

dropped = df.dropna(axis=1)
expected = df.loc[:, [0, 1, 3]]
inp = df.copy()
return_value = inp.dropna(axis=1, inplace=True)
tm.assert_frame_equal(dropped, expected)
tm.assert_frame_equal(inp, expected)
assert return_value is None

dropped = df.dropna(axis=0)
expected = df.loc[list(range(2, 6))]
inp = df.copy()
return_value = inp.dropna(axis=0, inplace=True)
tm.assert_frame_equal(dropped, expected)
tm.assert_frame_equal(inp, expected)
assert return_value is None

# threshold
dropped = df.dropna(axis=1, thresh=5)
expected = df.loc[:, [0, 1, 3]]
inp = df.copy()
return_value = inp.dropna(axis=1, thresh=5, inplace=True)
tm.assert_frame_equal(dropped, expected)
tm.assert_frame_equal(inp, expected)
assert return_value is None

dropped = df.dropna(axis=0, thresh=4)
expected = df.loc[range(2, 6)]
inp = df.copy()
return_value = inp.dropna(axis=0, thresh=4, inplace=True)
tm.assert_frame_equal(dropped, expected)
tm.assert_frame_equal(inp, expected)
assert return_value is None

dropped = df.dropna(axis=1, thresh=4)
tm.assert_frame_equal(dropped, df)

dropped = df.dropna(axis=1, thresh=3)
tm.assert_frame_equal(dropped, df)

# subset
dropped = df.dropna(axis=0, subset=[0, 1, 3])
inp = df.copy()
return_value = inp.dropna(axis=0, subset=[0, 1, 3], inplace=True)
tm.assert_frame_equal(dropped, df)
tm.assert_frame_equal(inp, df)
assert return_value is None

# all
dropped = df.dropna(axis=1, how="all")
tm.assert_frame_equal(dropped, df)

df[2] = np.nan
dropped = df.dropna(axis=1, how="all")
expected = df.loc[:, [0, 1, 3]]
tm.assert_frame_equal(dropped, expected)

# bad input
msg = "No axis named 3 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.dropna(axis=3)
