# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
idx = Index(range(3), name="foo")
result = idx.delete(1)
expected = idx[::2]
tm.assert_index_equal(result, expected, exact=True)

result = idx.delete(-2)
tm.assert_index_equal(result, expected, exact=True)
