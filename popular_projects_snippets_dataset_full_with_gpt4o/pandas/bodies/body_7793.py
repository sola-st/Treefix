# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
# here with_freq refers to being period_range-like
idx = PeriodIndex(
    ["2011-01-01", "2011-01-02", "2011-01-03"], freq=freq, name="idx"
)
self.check_sort_values_with_freq(idx)
