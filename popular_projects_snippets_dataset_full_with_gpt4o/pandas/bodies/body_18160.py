# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
pi = period_range("1994-04-01", periods=9, freq="19D")
expected = PeriodIndex(["NaT"] * 9, freq="19D")

obj = tm.box_expected(pi, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = obj + other
tm.assert_equal(result, expected)
result = other + obj
tm.assert_equal(result, expected)
result = obj - other
tm.assert_equal(result, expected)
msg = r"cannot subtract .* from .*"
with pytest.raises(TypeError, match=msg):
    other - obj

# some but not *all* NaT
other = other.copy()
other[0] = np.timedelta64(0, "ns")
expected = PeriodIndex([pi[0]] + ["NaT"] * 8, freq="19D")
expected = tm.box_expected(expected, box_with_array)

result = obj + other
tm.assert_equal(result, expected)
result = other + obj
tm.assert_equal(result, expected)
result = obj - other
tm.assert_equal(result, expected)
with pytest.raises(TypeError, match=msg):
    other - obj
