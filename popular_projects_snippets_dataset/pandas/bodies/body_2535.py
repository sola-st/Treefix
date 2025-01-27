# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py

df = timezone_frame
idx = df["B"].rename("foo")

# setitem
df["C"] = idx
tm.assert_series_equal(df["C"], Series(idx, name="C"))

df["D"] = "foo"
df["D"] = idx
tm.assert_series_equal(df["D"], Series(idx, name="D"))
del df["D"]

# assert that A & C are not sharing the same base (e.g. they
# are copies)
v1 = df._mgr.arrays[1]
v2 = df._mgr.arrays[2]
tm.assert_extension_array_equal(v1, v2)
v1base = v1._ndarray.base
v2base = v2._ndarray.base
assert v1base is None or (id(v1base) != id(v2base))

# with nan
df2 = df.copy()
df2.iloc[1, 1] = NaT
df2.iloc[1, 2] = NaT
result = df2["B"]
tm.assert_series_equal(notna(result), Series([True, False, True], name="B"))
tm.assert_series_equal(df2.dtypes, df.dtypes)
