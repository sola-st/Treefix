# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py

df = DataFrame({"A": range(10)})
ser = cut(df["A"], 5)
assert isinstance(ser.cat.categories, IntervalIndex)

# B & D end up as Categoricals
# the remainder are converted to in-line objects
# containing an IntervalIndex.values
df["B"] = ser
df["C"] = np.array(ser)
df["D"] = ser.values
df["E"] = np.array(ser.values)
df["F"] = ser.astype(object)

assert is_categorical_dtype(df["B"].dtype)
assert is_interval_dtype(df["B"].cat.categories)
assert is_categorical_dtype(df["D"].dtype)
assert is_interval_dtype(df["D"].cat.categories)

# These go through the Series constructor and so get inferred back
#  to IntervalDtype
assert is_interval_dtype(df["C"])
assert is_interval_dtype(df["E"])

# But the Series constructor doesn't do inference on Series objects,
#  so setting df["F"] doesn't get cast back to IntervalDtype
assert is_object_dtype(df["F"])

# they compare equal as Index
# when converted to numpy objects
c = lambda x: Index(np.array(x))
tm.assert_index_equal(c(df.B), c(df.B))
tm.assert_index_equal(c(df.B), c(df.C), check_names=False)
tm.assert_index_equal(c(df.B), c(df.D), check_names=False)
tm.assert_index_equal(c(df.C), c(df.D), check_names=False)

# B & D are the same Series
tm.assert_series_equal(df["B"], df["B"])
tm.assert_series_equal(df["B"], df["D"], check_names=False)

# C & E are the same Series
tm.assert_series_equal(df["C"], df["C"])
tm.assert_series_equal(df["C"], df["E"], check_names=False)
