# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_construction.py
# passing BooleanArray to coerce_to_array
values = np.array([True, False, True, False], dtype="bool")
mask = np.array([False, False, False, True], dtype="bool")
arr = BooleanArray(values, mask)
result = BooleanArray(*coerce_to_array(arr))
tm.assert_extension_array_equal(result, arr)
# no copy
assert result._data is arr._data
assert result._mask is arr._mask

result = BooleanArray(*coerce_to_array(arr), copy=True)
tm.assert_extension_array_equal(result, arr)
assert result._data is not arr._data
assert result._mask is not arr._mask

with pytest.raises(ValueError, match="cannot pass mask for BooleanArray input"):
    coerce_to_array(arr, mask=mask)
