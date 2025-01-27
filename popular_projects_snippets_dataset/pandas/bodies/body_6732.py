# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
result = index.astype(object)
expected = Index(index.values, dtype="object")
tm.assert_index_equal(result, expected)
assert not result.equals(index)
