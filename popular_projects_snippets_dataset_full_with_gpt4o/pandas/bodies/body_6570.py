# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
# in particular, this should not raise
arr = np.array(["A", "B", np.nan], dtype=object)
assert not com.is_bool_indexer(arr)
