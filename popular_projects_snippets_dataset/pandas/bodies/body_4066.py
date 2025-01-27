# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH 9201
df1 = DataFrame(np.random.randn(5, 3), columns=["foo", "bar", "baz"])
# Cast to object to avoid implicit cast when setting entry to "100" below
df1 = df1.astype({"foo": object})
# set one entry to a number in str format
df1.loc[0, "foo"] = "100"

df2 = DataFrame(np.random.randn(5, 3), columns=["foo", "bar", "baz"])
# Cast to object to avoid implicit cast when setting entry to "a" below
df2 = df2.astype({"foo": object})
# set one entry to a non-number str
df2.loc[0, "foo"] = "a"

result = getattr(df1, meth)(axis=1, numeric_only=True)
expected = getattr(df1[["bar", "baz"]], meth)(axis=1)
tm.assert_series_equal(expected, result)

result = getattr(df2, meth)(axis=1, numeric_only=True)
expected = getattr(df2[["bar", "baz"]], meth)(axis=1)
tm.assert_series_equal(expected, result)

# df1 has all numbers, df2 has a letter inside
msg = r"unsupported operand type\(s\) for -: 'float' and 'str'"
with pytest.raises(TypeError, match=msg):
    getattr(df1, meth)(axis=1, numeric_only=False)
msg = "could not convert string to float: 'a'"
with pytest.raises(TypeError, match=msg):
    getattr(df2, meth)(axis=1, numeric_only=False)
