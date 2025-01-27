# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py

ci = simple_index
categories = ci.categories

# test 0th element
result = ci.insert(0, "a")
expected = CategoricalIndex(list("aaabbca"), categories=categories)
tm.assert_index_equal(result, expected, exact=True)

# test Nth element that follows Python list behavior
result = ci.insert(-1, "a")
expected = CategoricalIndex(list("aabbcaa"), categories=categories)
tm.assert_index_equal(result, expected, exact=True)

# test empty
result = CategoricalIndex([], categories=categories).insert(0, "a")
expected = CategoricalIndex(["a"], categories=categories)
tm.assert_index_equal(result, expected, exact=True)

# invalid -> cast to object
expected = ci.astype(object).insert(0, "d")
result = ci.insert(0, "d")
tm.assert_index_equal(result, expected, exact=True)

# GH 18295 (test missing)
expected = CategoricalIndex(["a", np.nan, "a", "b", "c", "b"])
for na in (np.nan, pd.NaT, None):
    result = CategoricalIndex(list("aabcb")).insert(1, na)
    tm.assert_index_equal(result, expected)
