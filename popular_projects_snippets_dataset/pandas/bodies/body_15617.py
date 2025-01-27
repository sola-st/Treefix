# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_combine_first.py
# GH 41800
time_index = date_range(
    datetime(2021, 1, 1, 1),
    datetime(2021, 1, 1, 10),
    freq="H",
    tz="Europe/Rome",
)
s1 = Series(range(10), index=time_index)
s2 = Series(index=time_index)
result = s1.combine_first(s2)
tm.assert_series_equal(result, s1)
