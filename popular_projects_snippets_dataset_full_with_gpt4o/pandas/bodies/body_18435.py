# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#23320 special handling for timedelta64("NaT")
tz = tz_naive_fixture

dti = date_range("1994-04-01", periods=9, tz=tz, freq="QS")
other = np.timedelta64("NaT")
expected = DatetimeIndex(["NaT"] * 9, tz=tz)

obj = tm.box_expected(dti, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = obj + other
tm.assert_equal(result, expected)
result = other + obj
tm.assert_equal(result, expected)
result = obj - other
tm.assert_equal(result, expected)
msg = "cannot subtract"
with pytest.raises(TypeError, match=msg):
    other - obj
