# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
dti = pd.date_range("2016-01-01", periods=3)
tdi = TimedeltaIndex(["-1 Day"] * 3)
dtarr = dti.values
expected = DatetimeIndex(dtarr) - tdi

tdi = tm.box_expected(tdi, box_with_array)
expected = tm.box_expected(expected, box_with_array)

msg = "cannot subtract a datelike from"
with pytest.raises(TypeError, match=msg):
    tdi - dtarr

# TimedeltaIndex.__rsub__
result = dtarr - tdi
tm.assert_equal(result, expected)
