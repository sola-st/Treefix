# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py

# this takes the fast apply path

# cumsum (GH5614)
df = DataFrame([[1, 2, np.nan], [1, np.nan, 9], [3, 4, 9]], columns=["A", "B", "C"])
expected = DataFrame([[2, np.nan], [np.nan, 9], [4, 9]], columns=["B", "C"])
result = df.groupby("A").cumsum()
tm.assert_frame_equal(result, expected)

# GH 5755 - cumsum is a transformer and should ignore as_index
result = df.groupby("A", as_index=False).cumsum()
tm.assert_frame_equal(result, expected)

# GH 13994
result = df.groupby("A").cumsum(axis=1)
expected = df.cumsum(axis=1)
tm.assert_frame_equal(result, expected)
result = df.groupby("A").cumprod(axis=1)
expected = df.cumprod(axis=1)
tm.assert_frame_equal(result, expected)
