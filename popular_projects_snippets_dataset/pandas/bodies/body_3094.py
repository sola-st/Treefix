# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#13926
dates = date_range("2016-11-06", freq="H", periods=10, tz="US/Eastern")
obj = frame_or_series(dates)
res = obj.shift(ex)
exp = frame_or_series([NaT] * 10, dtype="datetime64[ns, US/Eastern]")
tm.assert_equal(res, exp)
assert tm.get_dtype(res) == "datetime64[ns, US/Eastern]"
