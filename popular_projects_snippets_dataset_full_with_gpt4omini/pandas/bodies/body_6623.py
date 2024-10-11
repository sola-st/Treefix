# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
idx = Index(range(2), name="foo")

result = idx.delete([1])
expected = Index(range(1), name="foo")
tm.assert_index_equal(result, expected, exact=True)

result = idx.delete(1)
tm.assert_index_equal(result, expected, exact=True)
