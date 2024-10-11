# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns a copy of old_shape with axis=0 multiplied by batch_size.

  Only use if this is the inner_shape of a DynamicRaggedShape.Spec with one
  or more row partitions.

  Args:
    old_shape: the original inner_shape.
    batch_size: the batch size.

  Returns:
    a new shape.
  """
head_dim = tensor_shape.dimension_at_index(old_shape, 0) * batch_size
exit(head_dim + old_shape[1:])
