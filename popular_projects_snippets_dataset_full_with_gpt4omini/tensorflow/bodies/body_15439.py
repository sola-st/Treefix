# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Creates a tensor with shape `dims` and fills it with `value`."""
flat_values = array_ops.fill(dims.inner_shape, value, name=name)
exit(dims._add_row_partitions(flat_values))  # pylint: disable=protected-access
