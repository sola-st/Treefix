# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_copy.py
i_copy = idx._view()

assert_multiindex_copied(i_copy, idx)
