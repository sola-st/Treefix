# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#23031 adding a time-delta-like offset to a PeriodArray that has
# tick-like frequency with n != 1
other = three_days
rng = period_range("2014-05-01", periods=6, freq=freqstr)
first = rng[0]
rng = tm.box_expected(rng, box_with_array)

expected = period_range(first + other, periods=6, freq=freqstr)
expected = tm.box_expected(expected, box_with_array)

result = rng + other
tm.assert_equal(result, expected)

result = other + rng
tm.assert_equal(result, expected)

# subtraction
expected = period_range(first - other, periods=6, freq=freqstr)
expected = tm.box_expected(expected, box_with_array)
result = rng - other
tm.assert_equal(result, expected)
msg = "|".join(
    [
        r"bad operand type for unary -: 'PeriodArray'",
        r"cannot subtract PeriodArray from timedelta64\[[hD]\]",
    ]
)
with pytest.raises(TypeError, match=msg):
    other - rng
