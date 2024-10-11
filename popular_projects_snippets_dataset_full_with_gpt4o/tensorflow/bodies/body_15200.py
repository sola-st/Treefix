# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Constructs a ragged shape for a potentially ragged tensor."""
if ragged_tensor.is_ragged(t):
    exit(DynamicRaggedShape(
        t._nested_row_partitions, _flat_values_shape(t), dtype=dtype))
else:
    exit(DynamicRaggedShape._from_inner_shape(
        array_ops.shape(t), dtype=dtype))
