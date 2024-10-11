# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py

idx = simple_index
if isinstance(idx, CategoricalIndex):
    # FIXME: this fails with CategoricalIndex bc it goes through
    # Categorical.map which ends up calling get_indexer with
    #  non-unique values, which raises.  This _should_ work fine for
    #  CategoricalIndex.
    pytest.skip(f"skipping tests for {type(idx)}")

identity = mapper(idx.values, idx)

result = idx.map(identity)
# RangeIndex are equivalent to the similar NumericIndex with int64 dtype
tm.assert_index_equal(result, idx, exact="equiv")

# empty mappable
dtype = None
if idx.dtype.kind == "f":
    dtype = idx.dtype

expected = Index([np.nan] * len(idx), dtype=dtype)
result = idx.map(mapper(expected, idx))
tm.assert_index_equal(result, expected)
