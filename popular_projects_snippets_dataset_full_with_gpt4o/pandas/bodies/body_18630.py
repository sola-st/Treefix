# Extracted from ./data/repos/pandas/pandas/tests/libs/test_lib.py
# GH#50592
left = np.array([0, 1, 2], dtype=dtype)
assert not lib.is_range_indexer(left, 2)
