# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
# Determined by cat ordering.
idx = CategoricalIndex(list("cab"), categories=list("cab"))
expected = np.arange(len(idx), dtype=np.intp)

actual = idx.get_indexer(idx)
tm.assert_numpy_array_equal(expected, actual)

with pytest.raises(ValueError, match="Invalid fill method"):
    idx.get_indexer(idx, method="invalid")
