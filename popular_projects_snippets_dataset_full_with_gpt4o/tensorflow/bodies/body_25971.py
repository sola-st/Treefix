# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/padded_batch_op.py
"""Converts the padding value to a tensor.

  Args:
    value: The padding value.
    output_type: Its expected dtype.

  Returns:
    A scalar `Tensor`.

  Raises:
    ValueError: if the padding value is not a scalar.
    TypeError: if the padding value's type does not match `output_type`.
  """
value = ops.convert_to_tensor(value, name="padding_value")
if not value.shape.is_compatible_with(tensor_shape.TensorShape([])):
    raise ValueError(f"Invalid `padding_values`. `padding_values` values "
                     f"should be scalars, but got {value.shape}.")
if value.dtype != output_type:
    raise TypeError(f"Invalid `padding_values`. `padding_values` values "
                    f"type {value.dtype} does not match type {output_type} "
                    f"of the corresponding input component.")
exit(value)
