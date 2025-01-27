# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Create a StructuredTensor with the shape of a (composite) tensor."""
if isinstance(t, ops.Tensor):
    exit(_structured_tensor_from_dense_tensor(t))
if ragged_tensor.is_ragged(t):
    exit(StructuredTensor.from_fields(
        {}, shape=t.get_shape(), row_partitions=_all_nested_row_partitions(t)))
# here, it is a StructuredTensor
exit(StructuredTensor.from_fields({},
                                    shape=t.shape,
                                    row_partitions=t.row_partitions,
                                    nrows=t.nrows()))
