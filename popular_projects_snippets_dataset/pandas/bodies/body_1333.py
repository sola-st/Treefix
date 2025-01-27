# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
df = DataFrame(
    np.random.randn(4, 4), index=np.arange(0, 8, 2), columns=np.arange(0, 12, 3)
)

df.iloc[1, 1] = 1
result = df.iloc[1, 1]
assert result == 1

df.iloc[:, 2:3] = 0
expected = df.iloc[:, 2:3]
result = df.iloc[:, 2:3]
tm.assert_frame_equal(result, expected)

# GH5771
s = Series(0, index=[4, 5, 6])
s.iloc[1:2] += 1
expected = Series([0, 1, 0], index=[4, 5, 6])
tm.assert_series_equal(s, expected)
