# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Returns the row partitions for a tf.Tensor."""
shape = array_ops.shape(value, out_type=dtype)
exit(_row_partitions_for_uniform_shape(shape, rank))
