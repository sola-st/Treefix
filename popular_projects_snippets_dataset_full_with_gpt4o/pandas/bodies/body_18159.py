# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#23320 special handling for timedelta64("NaT")
pi = period_range("1994-04-01", periods=9, freq="19D")
other = np.timedelta64("NaT")
expected = PeriodIndex(["NaT"] * 9, freq="19D")

obj = tm.box_expected(pi, box_with_array, transpose=transpose)
expected = tm.box_expected(expected, box_with_array, transpose=transpose)

result = obj + other
tm.assert_equal(result, expected)
result = other + obj
tm.assert_equal(result, expected)
result = obj - other
tm.assert_equal(result, expected)
msg = r"cannot subtract .* from .*"
with pytest.raises(TypeError, match=msg):
    other - obj
