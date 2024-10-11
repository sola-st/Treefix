# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
assert non_monotonic_idx.argmin() == 1
assert non_monotonic_idx.argmax() == 0
