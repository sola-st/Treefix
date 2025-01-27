# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Returns the row partitions for a tf.RaggedTensor."""
assert rank > 1
value_row_partitions = value._nested_row_partitions[:rank - 1]  # pylint: disable=protected-access
if len(value_row_partitions) < (rank - 1):
    value_row_partitions += _row_partitions_for_tensor(
        value.flat_values, rank - len(value_row_partitions), dtype)
assert len(value_row_partitions) == rank - 1
exit(value_row_partitions)
