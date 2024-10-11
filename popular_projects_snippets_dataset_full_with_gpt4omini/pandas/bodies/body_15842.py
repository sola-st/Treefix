# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
N = 100
ser = pd.Series(np.random.randn(N))
ser[0:4] = np.nan
ser[6:10] = 0

# replace list with a single value
return_value = ser.replace([np.nan], -1, inplace=True)
assert return_value is None

exp = ser.fillna(-1)
tm.assert_series_equal(ser, exp)

rs = ser.replace(0.0, np.nan)
ser[ser == 0.0] = np.nan
tm.assert_series_equal(rs, ser)

ser = pd.Series(np.fabs(np.random.randn(N)), tm.makeDateIndex(N), dtype=object)
ser[:5] = np.nan
ser[6:10] = "foo"
ser[20:30] = "bar"

# replace list with a single value
rs = ser.replace([np.nan, "foo", "bar"], -1)

assert (rs[:5] == -1).all()
assert (rs[6:10] == -1).all()
assert (rs[20:30] == -1).all()
assert (pd.isna(ser[:5])).all()

# replace with different values
rs = ser.replace({np.nan: -1, "foo": -2, "bar": -3})

assert (rs[:5] == -1).all()
assert (rs[6:10] == -2).all()
assert (rs[20:30] == -3).all()
assert (pd.isna(ser[:5])).all()

# replace with different values with 2 lists
rs2 = ser.replace([np.nan, "foo", "bar"], [-1, -2, -3])
tm.assert_series_equal(rs, rs2)

# replace inplace
return_value = ser.replace([np.nan, "foo", "bar"], -1, inplace=True)
assert return_value is None

assert (ser[:5] == -1).all()
assert (ser[6:10] == -1).all()
assert (ser[20:30] == -1).all()
