# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index_cls = self._index_cls

# scalar raise Exception
msg = (
    rf"{index_cls.__name__}\(\.\.\.\) must be called with a collection of some "
    "kind, 5 was passed"
)
with pytest.raises(TypeError, match=msg):
    index_cls(5)

# copy
# pass list, coerce fine
index = index_cls([-5, 0, 1, 2], dtype=dtype)
arr = index.values
new_index = index_cls(arr, copy=True)
tm.assert_index_equal(new_index, index, exact=True)
val = arr[0] + 3000

# this should not change index
arr[0] = val
assert new_index[0] != val

if dtype == np.int64:
    # pass list, coerce fine
    index = index_cls([-5, 0, 1, 2], dtype=dtype)
    expected = Index([-5, 0, 1, 2], dtype=dtype)
    tm.assert_index_equal(index, expected)

    # from iterable
    index = index_cls(iter([-5, 0, 1, 2]), dtype=dtype)
    expected = index_cls([-5, 0, 1, 2], dtype=dtype)
    tm.assert_index_equal(index, expected, exact=True)

    # interpret list-like
    expected = index_cls([5, 0], dtype=dtype)
    for cls in [Index, index_cls]:
        for idx in [
            cls([5, 0], dtype=dtype),
            cls(np.array([5, 0]), dtype=dtype),
            cls(Series([5, 0]), dtype=dtype),
        ]:
            tm.assert_index_equal(idx, expected)
