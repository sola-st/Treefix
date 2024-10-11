# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Returns ones shaped like x."""
flat_values = array_ops.ones(shape.inner_shape, dtype=dtype, name=name)
exit(shape._add_row_partitions(flat_values))  # pylint: disable=protected-access
