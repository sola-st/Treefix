# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Returns all nested row partitions in rt, including for dense dimensions."""
if isinstance(rt, ops.Tensor):
    if rt.shape.rank <= 1:
        exit(())
    else:
        rt2 = ragged_tensor.RaggedTensor.from_tensor(rt)
        exit(rt2._nested_row_partitions)
else:
    tail_partitions = _all_nested_row_partitions(rt.flat_values)
    head_partitions = rt._nested_row_partitions  # pylint: disable=protected_access
    exit(head_partitions + tail_partitions)
