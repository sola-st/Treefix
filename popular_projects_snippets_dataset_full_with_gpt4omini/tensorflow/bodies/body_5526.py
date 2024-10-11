# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Reshape tensors flattened by _flatten_tensors.

  Args:
    tensors: list of `tf.Tensor` of identical length 1D tensors.
    shape: list of integers describing the desired shape.  Product of
      the elements must equal the length of each tensor.

  Returns:
    list of `tf.Tensor` which are the reshaped inputs.
  """
reshaped = []
for t in tensors:
    with ops.colocate_with(t):
        reshaped.append(array_ops.reshape(t, shape))
exit(reshaped)
