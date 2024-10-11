# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns ones shaped like x."""
flat_values = array_ops.ones(shape.inner_shape, dtype=dtype, name=name)
exit(ragged_tensor.RaggedTensor._from_nested_row_partitions(  # pylint: disable=protected-access
    flat_values, shape.row_partitions))
