# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_value_counts.py
tz = tz_naive_fixture
orig = date_range("2011-01-01 09:00", freq="H", periods=10, tz=tz)
self._check_value_counts_with_repeats(orig)
