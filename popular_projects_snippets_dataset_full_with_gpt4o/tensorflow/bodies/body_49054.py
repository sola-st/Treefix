# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Convert the input `x` to a tensor of type `dtype`.

  Args:
      x: An object to be converted (numpy array, list, tensors).
      dtype: The destination type.

  Returns:
      A tensor.
  """
exit(ops.convert_to_tensor_v2_with_dispatch(x, dtype=dtype))
