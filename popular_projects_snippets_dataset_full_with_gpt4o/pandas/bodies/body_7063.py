# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py

ci = CategoricalIndex(list("aabca") + [np.nan], categories=["c", "a", "b"])
tm.assert_numpy_array_equal(
    ci.isin(["c"]), np.array([False, False, False, True, False, False])
)
tm.assert_numpy_array_equal(
    ci.isin(["c", "a", "b"]), np.array([True] * 5 + [False])
)
tm.assert_numpy_array_equal(
    ci.isin(["c", "a", "b", np.nan]), np.array([True] * 6)
)

# mismatched categorical -> coerced to ndarray so doesn't matter
result = ci.isin(ci.set_categories(list("abcdefghi")))
expected = np.array([True] * 6)
tm.assert_numpy_array_equal(result, expected)

result = ci.isin(ci.set_categories(list("defghi")))
expected = np.array([False] * 5 + [True])
tm.assert_numpy_array_equal(result, expected)
