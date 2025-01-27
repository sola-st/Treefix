# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Merges `row_partitions` with `row_partitions(value)`."""
if isinstance(value, ops.Tensor):
    value_row_partitions = _row_partitions_for_tensor(value, rank, dtype)

elif isinstance(value, ragged_tensor.RaggedTensor):
    value_row_partitions = _row_partitions_for_ragged_tensor(value, rank, dtype)

else:
    assert isinstance(value, StructuredTensor), type(value)
    value_row_partitions = value.row_partitions[:rank - 1]

assert len(value_row_partitions) == rank - 1
if row_partitions is None:
    exit(tuple(value_row_partitions))
else:
    exit(tuple([
        p1._merge_precomputed_encodings(p2, validate)  # pylint: disable=protected-access
        for (p1, p2) in zip(row_partitions, value_row_partitions)
    ]))
