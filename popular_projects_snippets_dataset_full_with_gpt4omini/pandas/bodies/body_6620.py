# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
idx = Index(range(4, 9, 2))

result = idx.insert(0, 2)
expected = Index(range(2, 9, 2))
tm.assert_index_equal(result, expected, exact=True)

result = idx.insert(3, 10)
expected = Index(range(4, 11, 2))
tm.assert_index_equal(result, expected, exact=True)
