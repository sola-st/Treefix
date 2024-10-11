# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH 23878
kwds = {kwd_name: 3} if kwd_name is not None else {}
p1_d = "19910905"
p2_d = "19920406"
freq = offset(n, normalize=False, **kwds)
p1 = PeriodIndex([p1_d], freq=freq)
p2 = PeriodIndex([p2_d], freq=freq)

result = p2 - p1
expected = PeriodIndex([p2_d], freq=freq.base) - PeriodIndex(
    [p1_d], freq=freq.base
)

tm.assert_index_equal(result, expected)
