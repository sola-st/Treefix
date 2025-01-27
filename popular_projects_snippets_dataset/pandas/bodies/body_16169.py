# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# check that Series.{opname} behaves like Series.__{opname}__,
tser = tm.makeTimeSeries().rename("ts")

series = ts[0](tser)
other = ts[1](tser)
check_reverse = ts[2]

op = getattr(Series, opname)
alt = getattr(operator, opname)

result = op(series, other)
expected = alt(series, other)
tm.assert_almost_equal(result, expected)
if check_reverse:
    rop = getattr(Series, "r" + opname)
    result = rop(series, other)
    expected = alt(other, series)
    tm.assert_almost_equal(result, expected)
