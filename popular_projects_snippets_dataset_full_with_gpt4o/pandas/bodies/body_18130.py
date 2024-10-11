# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH 23878
p1_d = "19910905"
p2_d = "19920406"
p1 = PeriodIndex([p1_d], freq=tick_classes(n))
p2 = PeriodIndex([p2_d], freq=tick_classes(n))

expected = PeriodIndex([p2_d], freq=p2.freq.base) - PeriodIndex(
    [p1_d], freq=p1.freq.base
)

tm.assert_index_equal((p2 - p1), expected)
