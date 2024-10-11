# Extracted from ./data/repos/pandas/pandas/tests/libs/test_lib.py
# GH#50592
left = np.arange(0, 100, dtype=dtype)
assert lib.is_range_indexer(left, 100)
