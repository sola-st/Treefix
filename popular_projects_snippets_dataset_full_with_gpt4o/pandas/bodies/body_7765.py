# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# GH 35392
axis = Index(idx)
actual = axis.get_indexer_for(target)
tm.assert_numpy_array_equal(actual, expected)
