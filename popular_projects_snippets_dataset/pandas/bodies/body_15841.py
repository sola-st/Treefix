# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#44498
ser = pd.Series([None, None, pd.Timestamp("2021-12-16 17:31")], dtype=object)
res = ser.replace({np.nan: None})  # should be a no-op
tm.assert_series_equal(res, ser)
assert res.dtype == object

# same thing but different calling convention
res = ser.replace(np.nan, None)
tm.assert_series_equal(res, ser)
assert res.dtype == object
