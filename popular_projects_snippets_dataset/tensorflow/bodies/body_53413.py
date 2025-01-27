# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Converts the given object to a `Tensor` or `CompositeTensor`.

  If `value` is a `CompositeTensor` it is returned unmodified.  Otherwise, it
  is converted to a `Tensor` using `convert_to_tensor()`.

  Args:
    value: A `CompositeTensor`, or an object that can be consumed by
      `convert_to_tensor()`.
    dtype: (Optional.) The required `DType` of the returned `Tensor` or
      `CompositeTensor`.
    name: (Optional.) A name to use if a new `Tensor` is created.
    as_ref: True if the caller wants the results as ref tensors.

  Returns:
    A `Tensor` or `CompositeTensor`, based on `value`.

  Raises:
    ValueError: If `dtype` does not match the element type of `value`.
  """
if isinstance(value, composite_tensor.CompositeTensor):
    value_dtype = getattr(value, "dtype", None)
    if dtype and not dtypes.as_dtype(dtype).is_compatible_with(value_dtype):
        raise ValueError(f"Tensor conversion dtype mismatch. "
                         f"Requested dtype is {dtypes.as_dtype(dtype).name}, "
                         f"Tensor has dtype {value.dtype.name}: {value!r}")
    exit(value)
else:
    exit(convert_to_tensor(
        value,
        dtype=dtype,
        name=name,
        as_ref=as_ref,
        accepted_result_types=(Tensor, composite_tensor.CompositeTensor)))
