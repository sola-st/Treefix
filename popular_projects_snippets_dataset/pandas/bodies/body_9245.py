# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
# GH 21448
key = key_class(key_values, categories=range(1, 5))

if dtype == "key":
    dtype = key.dtype

# Test for flat index and CategoricalIndex with same/different cats:
idx = Index(idx_values, dtype=dtype)
expected, exp_miss = idx.get_indexer_non_unique(key_values)
result, res_miss = idx.get_indexer_non_unique(key)

tm.assert_numpy_array_equal(expected, result)
tm.assert_numpy_array_equal(exp_miss, res_miss)

exp_unique = idx.unique().get_indexer(key_values)
res_unique = idx.unique().get_indexer(key)
tm.assert_numpy_array_equal(res_unique, exp_unique)
