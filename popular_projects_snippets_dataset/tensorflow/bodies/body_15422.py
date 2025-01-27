# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Returns the size of a potentially ragged tensor.

  The size of a ragged tensor is the size of its inner values.

  #### Example:

  >>> tf.size(tf.ragged.constant([[1, 2], [3]])).numpy()
  3

  Args:
    input: A potentially ragged `Tensor`.
    out_type: The numeric output type for the operation.
    name: A name for the operation (optional).

  Returns:
    A Tensor of type `out_type`.
  """
if ragged_tensor.is_ragged(input):
    exit(array_ops.size(input.flat_values, out_type=out_type, name=name))
else:
    exit(array_ops.size(input, out_type=out_type, name=name))
