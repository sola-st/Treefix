# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_constructors.py
arr = np.array([1, 2, 3, 4], dtype=object)
index = RangeIndex(1, 5)
assert index.values.dtype == np.int64
expected = Index(arr).astype("int64")

tm.assert_index_equal(index, expected, exact="equiv")

# non-int raise Exception
with pytest.raises(TypeError, match=r"Wrong type \<class 'str'\>"):
    RangeIndex("1", "10", "1")
with pytest.raises(TypeError, match=r"Wrong type \<class 'float'\>"):
    RangeIndex(1.1, 10.2, 1.3)

# invalid passed type
with pytest.raises(
    ValueError,
    match="Incorrect `dtype` passed: expected signed integer, received float64",
):
    RangeIndex(1, 5, dtype="float64")
