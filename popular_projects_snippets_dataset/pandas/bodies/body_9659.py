# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked_shared.py
arr = pd.array([1, 2, 3], dtype=dtype)
arr2 = pd.array([1, 2, pd.NA], dtype=dtype)

mask = arr == arr
mask2 = arr2 == arr2

result = np.zeros(3, dtype=bool)
result |= mask
# If MaskedArray.__array_ufunc__ handled "out" appropriately,
#  `result` should still be an ndarray.
assert isinstance(result, np.ndarray)
assert result.all()

# result |= mask worked because mask could be cast losslessly to
#  boolean ndarray. mask2 can't, so this raises
result = np.zeros(3, dtype=bool)
msg = "Specify an appropriate 'na_value' for this dtype"
with pytest.raises(ValueError, match=msg):
    result |= mask2

# addition
res = np.add(arr, arr2)
expected = pd.array([2, 4, pd.NA], dtype=dtype)
tm.assert_extension_array_equal(res, expected)

# when passing out=arr, we will modify 'arr' inplace.
res = np.add(arr, arr2, out=arr)
assert res is arr
tm.assert_extension_array_equal(res, expected)
tm.assert_extension_array_equal(arr, expected)
