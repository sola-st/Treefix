# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""A placeholder for the old StructuredTensorSpec."""
if not isinstance(field_specs, dict):
    raise TypeError('field_specs must be a dictionary.')
for k in field_specs.keys():
    if not isinstance(k, str):
        raise TypeError('field_specs must be a dictionary with string keys.')
for v in field_specs.values():
    if not isinstance(v, type_spec.TypeSpec):
        raise TypeError('field_specs must be a dictionary with TypeSpec values.')

shape = dynamic_ragged_shape.DynamicRaggedShape.Spec._from_tensor_shape(
    tensor_shape.as_shape(shape), 0, dtypes.int32)
rank = shape.rank
if rank is None:
    raise TypeError("StructuredTensor's shape must have known rank.")
for (k, v) in field_specs.items():
    field_shape_untruncated = _dynamic_ragged_shape_spec_from_spec(v)
    if field_shape_untruncated is None:
        raise ValueError(f'Cannot convert spec of {k}.')
    untruncated_rank = field_shape_untruncated.rank
    if (untruncated_rank is not None and untruncated_rank < rank):
        raise ValueError(f'Rank of field {k} is {untruncated_rank},'
                         f' but must be at least {rank}.')
    field_shape = field_shape_untruncated._truncate(rank)
    shape = shape._merge_with(field_shape)
exit(StructuredTensor.Spec(_ragged_shape=shape, _fields=field_specs))
