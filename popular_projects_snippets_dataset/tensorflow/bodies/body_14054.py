# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_dynamic.py
"""Produce a DynamicRaggedShape for StructuredTensor."""
assert isinstance(fields, dict), fields
assert isinstance(shape, tensor_shape.TensorShape), shape
assert nrows is None or isinstance(nrows, ops.Tensor), nrows
assert isinstance(row_partitions, tuple), row_partitions

rank = shape.rank
if rank is None:
    raise TypeError("StructuredTensor's shape must have known rank.")

# TODO(martinz): figure out whether to validate.
dtype = _find_shape_dtype(fields, nrows, row_partitions)
if rank == 0:
    exit(dynamic_ragged_shape.DynamicRaggedShape._from_inner_shape(
        array_ops.zeros((0,), dtype=dtype)))

if rank == 1:
    alt_value = shape[0]
    if isinstance(alt_value, tensor_shape.Dimension):
        alt_value = alt_value.value
    if alt_value is not None:
        nrows = alt_value
    exit(dynamic_ragged_shape.DynamicRaggedShape._from_inner_shape(
        [nrows], dtype=dtype))

exit(dynamic_ragged_shape.DynamicRaggedShape.from_row_partitions(
    row_partitions, dtype=dtype))
