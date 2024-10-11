# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH9068
index = Index([" jack", "jill ", " jesse ", "frank"])
expected = Index([getattr(str, method)(x) for x in index.values])

result = getattr(index.str, method)()
tm.assert_index_equal(result, expected)
