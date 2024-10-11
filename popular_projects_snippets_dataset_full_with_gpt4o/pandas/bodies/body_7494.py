# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_copy.py
i_copy = idx.copy()

assert_multiindex_copied(i_copy, idx)
