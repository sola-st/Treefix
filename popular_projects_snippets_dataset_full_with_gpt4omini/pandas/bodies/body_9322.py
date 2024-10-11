# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arrow_compat.py
arr = pa.array(data)
expected = pa.array(
    data.to_numpy(object, na_value=None),
    type=pa.from_numpy_dtype(data.dtype.numpy_dtype),
)
assert arr.equals(expected)
