# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Given fields, rank, and dtype, create a shape."""

field_shape = None
for (k, field) in fields.items():
    try:
        next_field_shape_raw = _dynamic_ragged_shape_from_tensor(
            field, dtype=dtype)
        next_field_shape = next_field_shape_raw[:rank]
        field_shape = _merge_with_optional(field_shape, next_field_shape)
    except Exception as err:
        raise ValueError(f'Error in shape of {k}') from err

exit(field_shape)
