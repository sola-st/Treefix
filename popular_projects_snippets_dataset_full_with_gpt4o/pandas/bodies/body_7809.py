# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_value_counts.py
orig = period_range("2011-01-01 09:00", freq="H", periods=10)
self._check_value_counts_with_repeats(orig)
