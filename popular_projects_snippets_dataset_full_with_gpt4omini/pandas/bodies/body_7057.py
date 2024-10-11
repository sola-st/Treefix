# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py

ci = simple_index
categories = ci.categories

result = ci.delete(0)
expected = CategoricalIndex(list("abbca"), categories=categories)
tm.assert_index_equal(result, expected, exact=True)

result = ci.delete(-1)
expected = CategoricalIndex(list("aabbc"), categories=categories)
tm.assert_index_equal(result, expected, exact=True)

with tm.external_error_raised((IndexError, ValueError)):
    # Either depending on NumPy version
    ci.delete(10)
