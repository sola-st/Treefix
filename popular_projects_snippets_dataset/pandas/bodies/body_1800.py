# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH 24127
n1_ = n1 * k
n2_ = n2 * k
s = Series(
    0,
    index=date_range("19910905 13:00", "19911005 07:00", freq=freq1).as_unit(unit),
)
s = s + range(len(s))

result1 = s.resample(str(n1_) + freq1).mean()
result2 = s.resample(str(n2_) + freq2).mean()
tm.assert_series_equal(result1, result2)
