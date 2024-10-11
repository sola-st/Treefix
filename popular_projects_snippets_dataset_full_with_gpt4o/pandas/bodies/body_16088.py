# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py

# both
index = date_range("20130101", periods=3, freq="D")
dti = date_range("20140204", periods=3, freq="s")
ser = Series(dti, index=index, name="xxx")
exp = Series(
    np.array([2014, 2014, 2014], dtype="int32"), index=index, name="xxx"
)
tm.assert_series_equal(ser.dt.year, exp)

exp = Series(np.array([2, 2, 2], dtype="int32"), index=index, name="xxx")
tm.assert_series_equal(ser.dt.month, exp)

exp = Series(np.array([0, 1, 2], dtype="int32"), index=index, name="xxx")
tm.assert_series_equal(ser.dt.second, exp)

exp = Series([ser[0]] * 3, index=index, name="xxx")
tm.assert_series_equal(ser.dt.normalize(), exp)
