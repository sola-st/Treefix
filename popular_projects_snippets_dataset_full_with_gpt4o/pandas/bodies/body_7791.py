# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
# GH#10295
idx = timedelta_range(start=f"1{freq}", periods=3, freq=freq).rename("idx")

self.check_sort_values_with_freq(idx)
