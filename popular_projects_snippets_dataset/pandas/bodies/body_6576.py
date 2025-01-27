# Extracted from ./data/repos/pandas/pandas/tests/indexes/object/test_indexing.py
index = Index(["b", "c"])
actual = index.get_indexer(["a", "b", "c", "d"], method=method)

tm.assert_numpy_array_equal(actual, expected)
