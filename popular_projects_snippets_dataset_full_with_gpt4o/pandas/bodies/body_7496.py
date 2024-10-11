# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_copy.py
i_view = idx.view()
assert_multiindex_copied(i_view, idx)
