# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#13926
dates = date_range("2016-11-06", freq="H", periods=10, tz="US/Eastern")
obj = frame_or_series(dates)

res = obj.shift(0)
tm.assert_equal(res, obj)
assert tm.get_dtype(res) == "datetime64[ns, US/Eastern]"

res = obj.shift(1)
exp_vals = [NaT] + dates.astype(object).values.tolist()[:9]
exp = frame_or_series(exp_vals)
tm.assert_equal(res, exp)
assert tm.get_dtype(res) == "datetime64[ns, US/Eastern]"

res = obj.shift(-2)
exp_vals = dates.astype(object).values.tolist()[2:] + [NaT, NaT]
exp = frame_or_series(exp_vals)
tm.assert_equal(res, exp)
assert tm.get_dtype(res) == "datetime64[ns, US/Eastern]"
