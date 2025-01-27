# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
"""Converts value to a `SparseTensor` or `Tensor`.

  Args:
    value: A `SparseTensor`, `SparseTensorValue`, or an object whose type has a
      registered `Tensor` conversion function.
    dtype: Optional element type for the returned tensor. If missing, the type
      is inferred from the type of `value`.
    name: Optional name to use if a new `Tensor` is created.

  Returns:
    A `SparseTensor` or `Tensor` based on `value`.

  Raises:
    RuntimeError: If result type is incompatible with `dtype`.
  """
if dtype is not None:
    dtype = dtypes.as_dtype(dtype)
if isinstance(value, SparseTensorValue):
    value = SparseTensor.from_value(value)
if isinstance(value, SparseTensor):
    if dtype and not dtype.is_compatible_with(value.dtype):
        raise RuntimeError(f"Sparse dtype mismatch. Requested: {dtype.name}, "
                           f" Actual: {value.dtype.name}")
    exit(value)
exit(ops.convert_to_tensor(value, dtype=dtype, name=name))
