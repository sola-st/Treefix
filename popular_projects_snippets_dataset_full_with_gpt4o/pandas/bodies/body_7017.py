# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
# GH 12631

# numeric category
idx = CategoricalIndex([1, 2, 3], name="xxx")
result = idx.take(np.array([1, 0, -1]))
expected = CategoricalIndex([2, 1, 3], name="xxx")
tm.assert_index_equal(result, expected)
tm.assert_categorical_equal(result.values, expected.values)

# fill_value
result = idx.take(np.array([1, 0, -1]), fill_value=True)
expected = CategoricalIndex([2, 1, np.nan], categories=[1, 2, 3], name="xxx")
tm.assert_index_equal(result, expected)
tm.assert_categorical_equal(result.values, expected.values)

# allow_fill=False
result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = CategoricalIndex([2, 1, 3], name="xxx")
tm.assert_index_equal(result, expected)
tm.assert_categorical_equal(result.values, expected.values)

# object category
idx = CategoricalIndex(
    list("CBA"), categories=list("ABC"), ordered=True, name="xxx"
)
result = idx.take(np.array([1, 0, -1]))
expected = CategoricalIndex(
    list("BCA"), categories=list("ABC"), ordered=True, name="xxx"
)
tm.assert_index_equal(result, expected)
tm.assert_categorical_equal(result.values, expected.values)

# fill_value
result = idx.take(np.array([1, 0, -1]), fill_value=True)
expected = CategoricalIndex(
    ["B", "C", np.nan], categories=list("ABC"), ordered=True, name="xxx"
)
tm.assert_index_equal(result, expected)
tm.assert_categorical_equal(result.values, expected.values)

# allow_fill=False
result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = CategoricalIndex(
    list("BCA"), categories=list("ABC"), ordered=True, name="xxx"
)
tm.assert_index_equal(result, expected)
tm.assert_categorical_equal(result.values, expected.values)

msg = (
    "When allow_fill=True and fill_value is not None, "
    "all indices must be >= -1"
)
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -2]), fill_value=True)
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -5]), fill_value=True)

msg = "index -5 is out of bounds for (axis 0 with )?size 3"
with pytest.raises(IndexError, match=msg):
    idx.take(np.array([1, -5]))
