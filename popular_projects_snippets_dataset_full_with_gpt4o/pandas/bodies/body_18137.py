# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#18824
pi = PeriodIndex([Period("2015Q1"), Period("2016Q2")])
other = box(
    [
        pd.offsets.QuarterEnd(n=1, startingMonth=12),
        pd.offsets.QuarterEnd(n=-2, startingMonth=12),
    ]
)

expected = PeriodIndex([pi[n] - other[n] for n in range(len(pi))])
expected = expected.astype(object)

with tm.assert_produces_warning(PerformanceWarning):
    res = pi - other
tm.assert_index_equal(res, expected)

anchored = box([pd.offsets.MonthEnd(), pd.offsets.Day(n=2)])

# addition/subtraction ops with anchored offsets should issue
# a PerformanceWarning and _then_ raise a TypeError.
msg = r"Input has different freq=-1M from Period\(freq=Q-DEC\)"
with pytest.raises(IncompatibleFrequency, match=msg):
    with tm.assert_produces_warning(PerformanceWarning):
        pi - anchored
with pytest.raises(IncompatibleFrequency, match=msg):
    with tm.assert_produces_warning(PerformanceWarning):
        anchored - pi
