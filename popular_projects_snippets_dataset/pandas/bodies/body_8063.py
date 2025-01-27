# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 12756
expected = Index(["foo", "bar", "baz"])
index = tm.makeIntIndex(3)
result = index.map(mapper(expected.values, index))
tm.assert_index_equal(result, expected)
