# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
df = DataFrame(
    np.random.randn(10, 4), index=list("abcdefghij"), columns=list("ABCD")
)

df.iloc[1, 1] = 1
result = df.iloc[1, 1]
assert result == 1

df.iloc[:, 2:3] = 0
expected = df.iloc[:, 2:3]
result = df.iloc[:, 2:3]
tm.assert_frame_equal(result, expected)

s = Series(np.random.randn(10), index=range(0, 20, 2))

s.iloc[1] = 1
result = s.iloc[1]
assert result == 1

s.iloc[:4] = 0
expected = s.iloc[:4]
result = s.iloc[:4]
tm.assert_series_equal(result, expected)

s = Series([-1] * 6)
s.iloc[0::2] = [0, 2, 4]
s.iloc[1::2] = [1, 3, 5]
result = s
expected = Series([0, 1, 2, 3, 4, 5])
tm.assert_series_equal(result, expected)
