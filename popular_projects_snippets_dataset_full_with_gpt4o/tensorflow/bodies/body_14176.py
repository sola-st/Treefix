# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Creates a spec of a StructuredTensor with fields and rank."""
shape = None
for (k, v) in fields.items():
    field_shape_untruncated = _dynamic_ragged_shape_spec_from_spec(v)
    if field_shape_untruncated is None:
        raise ValueError(f'Cannot convert spec of {k}.')
    untruncated_rank = field_shape_untruncated.rank
    if (untruncated_rank is not None and untruncated_rank < rank):
        raise ValueError(f'Rank of field {k} is {untruncated_rank}, '
                         f'but must be at least {rank}.')
    field_shape = field_shape_untruncated._truncate(rank)  # pylint: disable=protected-access
    if shape is None:
        shape = field_shape
    else:
        shape = shape._merge_with(field_shape)
exit(StructuredTensor.Spec(_ragged_shape=shape, _fields=fields))
