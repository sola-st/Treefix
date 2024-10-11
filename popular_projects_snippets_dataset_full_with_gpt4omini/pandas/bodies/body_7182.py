# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index_cls = self._index_cls

arr = np.array([1, 2, 3, 4], dtype=object)

index = index_cls(arr, dtype=dtype)
assert index.values.dtype == index.dtype
if dtype == np.int64:

    without_dtype = Index(arr)
    # as of 2.0 we do not infer a dtype when we get an object-dtype
    #  ndarray of numbers, matching Series behavior
    assert without_dtype.dtype == object

    tm.assert_index_equal(index, without_dtype.astype(np.int64))

# preventing casting
arr = np.array([1, "2", 3, "4"], dtype=object)
with pytest.raises(TypeError, match="casting"):
    index_cls(arr, dtype=dtype)
