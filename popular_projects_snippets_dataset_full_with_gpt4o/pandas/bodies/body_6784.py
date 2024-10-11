# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 23576
year_2017 = Interval(
    Timestamp("2017-01-01 00:00:00"), Timestamp("2018-01-01 00:00:00")
)
year_2017_index = IntervalIndex([year_2017])
assert not year_2017_index._is_all_dates
