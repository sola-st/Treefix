# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py

# GH 5104
# make sure that we are actually changing the object
s_orig = Series([1, 2, 3])
df_orig = DataFrame(np.random.randint(0, 5, size=10).reshape(-1, 5))

# no dtype change
s = s_orig.copy()
s2 = s
s += 1
tm.assert_series_equal(s, s2)
tm.assert_series_equal(s_orig + 1, s)
assert s is s2
assert s._mgr is s2._mgr

df = df_orig.copy()
df2 = df
df += 1
tm.assert_frame_equal(df, df2)
tm.assert_frame_equal(df_orig + 1, df)
assert df is df2
assert df._mgr is df2._mgr

# dtype change
s = s_orig.copy()
s2 = s
s += 1.5
tm.assert_series_equal(s, s2)
tm.assert_series_equal(s_orig + 1.5, s)

df = df_orig.copy()
df2 = df
df += 1.5
tm.assert_frame_equal(df, df2)
tm.assert_frame_equal(df_orig + 1.5, df)
assert df is df2
assert df._mgr is df2._mgr

# mixed dtype
arr = np.random.randint(0, 10, size=5)
df_orig = DataFrame({"A": arr.copy(), "B": "foo"})
df = df_orig.copy()
df2 = df
df["A"] += 1
expected = DataFrame({"A": arr.copy() + 1, "B": "foo"})
tm.assert_frame_equal(df, expected)
tm.assert_frame_equal(df2, expected)
assert df._mgr is df2._mgr

df = df_orig.copy()
df2 = df
df["A"] += 1.5
expected = DataFrame({"A": arr.copy() + 1.5, "B": "foo"})
tm.assert_frame_equal(df, expected)
tm.assert_frame_equal(df2, expected)
assert df._mgr is df2._mgr
