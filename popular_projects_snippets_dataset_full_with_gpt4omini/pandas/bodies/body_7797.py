# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
tz = tz_naive_fixture

# without freq
idx = DatetimeIndex(index_dates, tz=tz, name="idx")
expected = DatetimeIndex(expected_dates, tz=tz, name="idx")

self.check_sort_values_without_freq(idx, expected)
