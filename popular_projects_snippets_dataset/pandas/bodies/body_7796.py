# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
# GH#10295

idx = TimedeltaIndex(
    ["1 hour", "3 hour", "5 hour", "2 hour ", "1 hour"], name="idx1"
)
expected = TimedeltaIndex(
    ["1 hour", "1 hour", "2 hour", "3 hour", "5 hour"], name="idx1"
)
self.check_sort_values_without_freq(idx, expected)
