# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_duplicates.py
result = idx_dup.duplicated(keep=keep)
tm.assert_numpy_array_equal(result, expected)
