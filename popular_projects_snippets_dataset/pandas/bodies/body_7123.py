# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH 18630
idx = simple_index
if name:
    idx = idx.rename(name)

# standard categories
dtype = CategoricalDtype(ordered=ordered)
result = idx.astype(dtype, copy=copy)
expected = CategoricalIndex(idx, name=name, ordered=ordered)
tm.assert_index_equal(result, expected, exact=True)

# non-standard categories
dtype = CategoricalDtype(idx.unique().tolist()[:-1], ordered)
result = idx.astype(dtype, copy=copy)
expected = CategoricalIndex(idx, name=name, dtype=dtype)
tm.assert_index_equal(result, expected, exact=True)

if ordered is False:
    # dtype='category' defaults to ordered=False, so only test once
    result = idx.astype("category", copy=copy)
    expected = CategoricalIndex(idx, name=name)
    tm.assert_index_equal(result, expected, exact=True)
