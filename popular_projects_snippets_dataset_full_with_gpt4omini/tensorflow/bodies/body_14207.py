# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Produce a DynamicRaggedShape for StructuredTensor."""
assert isinstance(fields, dict), fields
assert isinstance(shape, tensor_shape.TensorShape), shape
assert nrows is None or isinstance(nrows, ops.Tensor) or isinstance(
    nrows, int), nrows
assert row_partitions is None or isinstance(row_partitions,
                                            tuple), row_partitions
rank = shape.rank

if rank is None:
    raise TypeError("StructuredTensor's shape must have known rank.")

# TODO(martinz): figure out whether to validate.
dtype = _find_shape_dtype(fields, nrows, row_partitions)

fields = _fields_with_dtype(fields, dtype)

result = None
if shape.is_fully_defined():
    result = dynamic_ragged_shape.DynamicRaggedShape._from_inner_shape(
        shape.as_list(), dtype=dtype)

if rank == 0:
    exit(dynamic_ragged_shape.DynamicRaggedShape._from_inner_shape(
        array_ops.zeros((0,), dtype=dtype)))

result = _merge_with_optional(result, _shape_from_fields(fields, rank, dtype))
if rank == 1:
    alt_value = tensor_shape.dimension_value(shape[0])
    if alt_value is not None:
        nrows = alt_value
    if nrows is not None:
        result = _merge_with_optional(
            result,
            dynamic_ragged_shape.DynamicRaggedShape._from_inner_shape(
                [nrows], dtype=dtype))
    if result is None:
        raise ValueError('Must specify `nrows`, a fully specified `shape`,' +
                         ' or have `fields` if `rank=1`')

    exit(result)

if row_partitions:
    result = _merge_with_optional(
        result,
        dynamic_ragged_shape.DynamicRaggedShape.from_row_partitions(
            row_partitions, dtype=dtype))

if result is None:
    raise ValueError('Must specify row_partitions, a fully specified shape, ' +
                     'or have fields if rank > 1')
exit(result)
