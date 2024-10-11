# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#23031 adding a time-delta-like offset to a PeriodArray that has
# minute frequency with n != 1.  A more general case is tested below
# in test_pi_add_timedeltalike_tick_gt1, but here we write out the
# expected result more explicitly.
other = three_days
rng = period_range("2014-05-01", periods=3, freq="2D")
rng = tm.box_expected(rng, box_with_array)

expected = PeriodIndex(["2014-05-04", "2014-05-06", "2014-05-08"], freq="2D")
expected = tm.box_expected(expected, box_with_array)

result = rng + other
tm.assert_equal(result, expected)

result = other + rng
tm.assert_equal(result, expected)

# subtraction
expected = PeriodIndex(["2014-04-28", "2014-04-30", "2014-05-02"], freq="2D")
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
