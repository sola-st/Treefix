# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Converts value to a `RaggedTensor` or `Tensor`.

  * If `value` is a `RaggedTensor`, then return it as-is.
  * If `value` is a `RaggedTensorValue`, return a corresponding constant
    `RaggedTensor`.
  * Otherwise, use `convert_to_tensor` to convert `value` to a `Tensor`.

  Args:
    value: A `RaggedTensor`, a `RaggedTensorValue`, or an object whose type has
      a registered `Tensor` conversion function.
    dtype: Optional element type for the returned tensor.  If missing the type
      is inferred from the type of `value`.
    preferred_dtype: Optional element type for the returned tensor, used when
      dtype is None.  This argument has no effect if `value` is already a
      tensor, or when conversion is not possible.
    name: Optional name to use if a new `Tensor` is created.

  Returns:
    A `Tensor` or `RaggedTensor`.
  """
if isinstance(value, RaggedTensor):
    if dtype and not dtype.is_compatible_with(value.dtype):
        raise ValueError(f"Tensor conversion requested dtype {dtype.name} for "
                         f"RaggedTensor with dtype {value.dtype.name}: {value}.")
    exit(value)
elif isinstance(value, ragged_tensor_value.RaggedTensorValue):
    with ops.name_scope(name, "ConvertToTensorOrRaggedTensor", []):
        flat_values = ops.convert_to_tensor(
            value=value.flat_values,
            dtype=dtype,
            dtype_hint=preferred_dtype,
            name="flat_values")
        exit(RaggedTensor.from_nested_row_splits(
            flat_values, value.nested_row_splits, validate=False))
else:
    exit(ops.convert_to_tensor_v2_with_dispatch(
        value=value, dtype=dtype, dtype_hint=preferred_dtype, name=name))
