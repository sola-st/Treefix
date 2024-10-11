# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_astype.py
# GH#18630
index = CategoricalIndex(
    list("aabbca"), categories=list("cab"), ordered=index_ordered
)
if name:
    index = index.rename(name)

# standard categories
dtype = CategoricalDtype(ordered=dtype_ordered)
result = index.astype(dtype)
expected = CategoricalIndex(
    index.tolist(),
    name=name,
    categories=index.categories,
    ordered=dtype_ordered,
)
tm.assert_index_equal(result, expected)

# non-standard categories
dtype = CategoricalDtype(index.unique().tolist()[:-1], dtype_ordered)
result = index.astype(dtype)
expected = CategoricalIndex(index.tolist(), name=name, dtype=dtype)
tm.assert_index_equal(result, expected)

if dtype_ordered is False:
    # dtype='category' can't specify ordered, so only test once
    result = index.astype("category")
    expected = index
    tm.assert_index_equal(result, expected)
