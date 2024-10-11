# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
df = DataFrame([[1, 3, 2], [1, 2, 3]])
expected = DataFrame([[1.0, 3.0, 2.0], [1, 2, 3]]) / 3.0
result = df.rank(1, pct=True)
tm.assert_frame_equal(result, expected)

df = DataFrame([[1, 3, 2], [1, 2, 3]])
expected = df.rank(0) / 2.0
result = df.rank(0, pct=True)
tm.assert_frame_equal(result, expected)

df = DataFrame([["b", "c", "a"], ["a", "c", "b"]])
expected = DataFrame([[2.0, 3.0, 1.0], [1, 3, 2]])
result = df.rank(1, numeric_only=False)
tm.assert_frame_equal(result, expected)

expected = DataFrame([[2.0, 1.5, 1.0], [1, 1.5, 2]])
result = df.rank(0, numeric_only=False)
tm.assert_frame_equal(result, expected)

df = DataFrame([["b", np.nan, "a"], ["a", "c", "b"]])
expected = DataFrame([[2.0, np.nan, 1.0], [1.0, 3.0, 2.0]])
result = df.rank(1, numeric_only=False)
tm.assert_frame_equal(result, expected)

expected = DataFrame([[2.0, np.nan, 1.0], [1.0, 1.0, 2.0]])
result = df.rank(0, numeric_only=False)
tm.assert_frame_equal(result, expected)

# f7u12, this does not work without extensive workaround
data = [
    [datetime(2001, 1, 5), np.nan, datetime(2001, 1, 2)],
    [datetime(2000, 1, 2), datetime(2000, 1, 3), datetime(2000, 1, 1)],
]
df = DataFrame(data)

# check the rank
expected = DataFrame([[2.0, np.nan, 1.0], [2.0, 3.0, 1.0]])
result = df.rank(1, numeric_only=False, ascending=True)
tm.assert_frame_equal(result, expected)

expected = DataFrame([[1.0, np.nan, 2.0], [2.0, 1.0, 3.0]])
result = df.rank(1, numeric_only=False, ascending=False)
tm.assert_frame_equal(result, expected)

df = DataFrame({"a": [1e-20, -5, 1e-20 + 1e-40, 10, 1e60, 1e80, 1e-30]})
exp = DataFrame({"a": [3.5, 1.0, 3.5, 5.0, 6.0, 7.0, 2.0]})
tm.assert_frame_equal(df.rank(), exp)
