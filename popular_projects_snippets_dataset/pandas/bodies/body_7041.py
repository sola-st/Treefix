# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_constructors.py

ci = CategoricalIndex(list("aabbca"), categories=list("abcd"), ordered=False)
categories = ci.categories

result = Index(ci)
tm.assert_index_equal(result, ci, exact=True)
assert not result.ordered

result = Index(ci.values)
tm.assert_index_equal(result, ci, exact=True)
assert not result.ordered

# empty
result = CategoricalIndex([], categories=categories)
tm.assert_index_equal(result.categories, Index(categories))
tm.assert_numpy_array_equal(result.codes, np.array([], dtype="int8"))
assert not result.ordered

# passing categories
result = CategoricalIndex(list("aabbca"), categories=categories)
tm.assert_index_equal(result.categories, Index(categories))
tm.assert_numpy_array_equal(
    result.codes, np.array([0, 0, 1, 1, 2, 0], dtype="int8")
)

c = Categorical(list("aabbca"))
result = CategoricalIndex(c)
tm.assert_index_equal(result.categories, Index(list("abc")))
tm.assert_numpy_array_equal(
    result.codes, np.array([0, 0, 1, 1, 2, 0], dtype="int8")
)
assert not result.ordered

result = CategoricalIndex(c, categories=categories)
tm.assert_index_equal(result.categories, Index(categories))
tm.assert_numpy_array_equal(
    result.codes, np.array([0, 0, 1, 1, 2, 0], dtype="int8")
)
assert not result.ordered

ci = CategoricalIndex(c, categories=list("abcd"))
result = CategoricalIndex(ci)
tm.assert_index_equal(result.categories, Index(categories))
tm.assert_numpy_array_equal(
    result.codes, np.array([0, 0, 1, 1, 2, 0], dtype="int8")
)
assert not result.ordered

result = CategoricalIndex(ci, categories=list("ab"))
tm.assert_index_equal(result.categories, Index(list("ab")))
tm.assert_numpy_array_equal(
    result.codes, np.array([0, 0, 1, 1, -1, 0], dtype="int8")
)
assert not result.ordered

result = CategoricalIndex(ci, categories=list("ab"), ordered=True)
tm.assert_index_equal(result.categories, Index(list("ab")))
tm.assert_numpy_array_equal(
    result.codes, np.array([0, 0, 1, 1, -1, 0], dtype="int8")
)
assert result.ordered

result = CategoricalIndex(ci, categories=list("ab"), ordered=True)
expected = CategoricalIndex(
    ci, categories=list("ab"), ordered=True, dtype="category"
)
tm.assert_index_equal(result, expected, exact=True)

# turn me to an Index
result = Index(np.array(ci))
assert isinstance(result, Index)
assert not isinstance(result, CategoricalIndex)
