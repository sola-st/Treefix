# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# GH 34019
n = DataFrame([[1, 2], [1, 2]]).set_index([0, 1]).index.nunique()
assert n == 1
