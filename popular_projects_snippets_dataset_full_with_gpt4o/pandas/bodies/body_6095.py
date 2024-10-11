# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
fill_value = data_missing[1]  # valid
na = data_missing[0]

arr = data_missing._from_sequence(
    [na, fill_value, na], dtype=data_missing.dtype
)
result = arr.take([-1, 1], fill_value=fill_value, allow_fill=True)
expected = arr.take([1, 1])
self.assert_extension_array_equal(result, expected)
