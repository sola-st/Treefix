# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_append.py
# with objects
result = ci.append(Index(["c", "a"]))
expected = CategoricalIndex(list("aabbcaca"), categories=ci.categories)
tm.assert_index_equal(result, expected, exact=True)
