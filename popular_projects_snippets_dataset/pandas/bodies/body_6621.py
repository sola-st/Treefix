# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
# insert in the middle
idx = Index(range(0, 3, 2))
result = idx.insert(1, 1)
expected = Index(range(3))
tm.assert_index_equal(result, expected, exact=True)

idx = idx * 2
result = idx.insert(1, 2)
expected = expected * 2
tm.assert_index_equal(result, expected, exact=True)
