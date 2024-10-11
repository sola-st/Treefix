# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py

ci = CategoricalIndex(list("aabbca"), categories=list("cabdef"))
result = ci.set_categories(list("cab"))
tm.assert_index_equal(
    result, CategoricalIndex(list("aabbca"), categories=list("cab"))
)

ci = CategoricalIndex(list("aabbca"), categories=list("cab"))
result = ci.rename_categories(list("efg"))
tm.assert_index_equal(
    result, CategoricalIndex(list("ffggef"), categories=list("efg"))
)

# GH18862 (let rename_categories take callables)
result = ci.rename_categories(lambda x: x.upper())
tm.assert_index_equal(
    result, CategoricalIndex(list("AABBCA"), categories=list("CAB"))
)

ci = CategoricalIndex(list("aabbca"), categories=list("cab"))
result = ci.add_categories(["d"])
tm.assert_index_equal(
    result, CategoricalIndex(list("aabbca"), categories=list("cabd"))
)

ci = CategoricalIndex(list("aabbca"), categories=list("cab"))
result = ci.remove_categories(["c"])
tm.assert_index_equal(
    result,
    CategoricalIndex(list("aabb") + [np.nan] + ["a"], categories=list("ab")),
)

ci = CategoricalIndex(list("aabbca"), categories=list("cabdef"))
result = ci.as_unordered()
tm.assert_index_equal(result, ci)

ci = CategoricalIndex(list("aabbca"), categories=list("cabdef"))
result = ci.as_ordered()
tm.assert_index_equal(
    result,
    CategoricalIndex(list("aabbca"), categories=list("cabdef"), ordered=True),
)

# invalid
msg = "cannot use inplace with CategoricalIndex"
with pytest.raises(ValueError, match=msg):
    ci.set_categories(list("cab"), inplace=True)
