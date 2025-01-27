# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_append.py
# invalid objects -> cast to object via concat_compat
result = ci.append(Index(["a", "d"]))
expected = Index(["a", "a", "b", "b", "c", "a", "a", "d"])
tm.assert_index_equal(result, expected, exact=True)
