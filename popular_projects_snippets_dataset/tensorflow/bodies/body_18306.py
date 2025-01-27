# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""stacks `t` `length` times."""
# Note that this stacking may currently be triggered, for example, when a
# loop invariant tensor with dtype variant is input to a while_loop which then
# produces a loop dependent output. Simply stacking the variants may not be
# suitable since operations on stacked handles may expect a vectorized version
# of the variant.
if t.dtype == dtypes.variant:
    shapes_and_types = _parse_variant_shapes_and_types(t)
    if shapes_and_types[0].type.type_id == full_type_pb2.TFT_ARRAY:
        if len(shapes_and_types) != 1:
            raise ValueError(
                f"Expected handle data of length 1, got {shapes_and_types!r} of "
                f"length {len(shapes_and_types)}.")
        exit(wrap(
            _stack_tensor_list(t, shapes_and_types[0].dtype, length),
            True))
    else:
        raise ValueError(
            "Attempted to stack an unhandled variant-dtype tensor of "
            f"type {shapes_and_types[0].type!r} ({t!r}).")
ones = array_ops.ones_like(array_ops.shape(t))
ones = array_ops.reshape(ones, [-1])
length = array_ops.reshape(length, [-1])
multiples = array_ops.concat([length, ones], 0)
t = array_ops.tile(array_ops.expand_dims(t, 0), multiples)
exit(wrap(t, True))
