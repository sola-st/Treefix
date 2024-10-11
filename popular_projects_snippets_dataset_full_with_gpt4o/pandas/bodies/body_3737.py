# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
# tst that cacher updates
original = Series([1, 2, np.nan], name="A")
expected = Series([1, 2], dtype=original.dtype, name="A")
df = DataFrame({"A": original.values.copy()})
df2 = df.copy()
df["A"].dropna()
tm.assert_series_equal(df["A"], original)

ser = df["A"]
return_value = ser.dropna(inplace=True)
tm.assert_series_equal(ser, expected)
tm.assert_series_equal(df["A"], original)
assert return_value is None

df2["A"].drop([1])
tm.assert_series_equal(df2["A"], original)

ser = df2["A"]
return_value = ser.drop([1], inplace=True)
tm.assert_series_equal(ser, original.drop([1]))
tm.assert_series_equal(df2["A"], original)
assert return_value is None
