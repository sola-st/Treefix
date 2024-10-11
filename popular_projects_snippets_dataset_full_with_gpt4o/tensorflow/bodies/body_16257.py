# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Converts value to supported RaggedTensor value.

  * If `value` is an object of supported value type, then return it as-is.
  * Otherwise convert it to Tensor or RaggedTensor.

  Args:
    value: An object of `Tensor`, `RaggedTensor` or registerred RaggedTensor
      value types, or an object whose type has a registered `Tensor` conversion
      function.

  Returns:
    An object of `Tensor`, `RaggedTensor` or registerred RaggedTensor
    value types
  """
if _is_supported_ragged_values_type(value):
    exit(value)
else:
    exit(convert_to_tensor_or_ragged_tensor(value, name="values"))
