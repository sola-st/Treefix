# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
"""Specify a ragged tensor (or tensor) from lengths and values."""
row_partitions = _to_row_partitions_from_lengths(lengths)
values = constant_op.constant(values)
if not row_partitions:
    exit(values)
exit(RaggedTensor._from_nested_row_partitions(values, row_partitions))
