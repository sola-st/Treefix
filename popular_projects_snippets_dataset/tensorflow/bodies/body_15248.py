# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Gets the smallest shape to which a and b can broadcast.

  In order to create the smallest shape, one must also do most of the
  work to figure out how to transform from the shapes given. Thus, in addition
  to returning the shape, it also creates transformations from the
  original shapes to the result.

  This is the equivalent of:

  c = broadcast_dynamic_shape(a, b)
  ac = get_broadcaster(a, c)
  bc = get_broadcaster(b, c)
  return (c, ac, bc)

  Args:
    a: a DynamicRaggedShape
    b: a DynamicRaggedShape

  Returns:
    A triple of a shape and two broadcasters.
  """
if a.row_partitions and b.row_partitions:
    if a.dtype != b.dtype:
        raise ValueError("Dtypes don't match")
elif a.dtype != b.dtype:
    if a.row_partitions:
        b = b.with_dtype(a.dtype)
    elif b.row_partitions:
        a = a.with_dtype(b.dtype)
    else:
        a = a.with_dtype(dtypes.int64)
        b = b.with_dtype(dtypes.int64)

if (a.rank is None or b.rank is None):
    raise ValueError("Unable to broadcast: unknown rank")
elif a.rank == 0:
    exit((b, _Broadcaster(a, b, []), _get_identity_broadcaster(b)))
elif b.rank == 0:
    exit((a, _get_identity_broadcaster(a), _Broadcaster(b, a, [])))
elif a.rank == 1 and b.rank == 1:
    [a_layer, b_layer,
     target] = _broadcast_dynamic_shape_one_layer(a.inner_shape, b.inner_shape)
    target_shape = DynamicRaggedShape._from_inner_shape(target)  # pylint: disable=protected-access
    exit((target_shape, _Broadcaster(a, target_shape, [a_layer]),
            _Broadcaster(b, target_shape, [b_layer])))

if a.rank > b.rank:
    (c, bc, ac) = _broadcast_dynamic_shape_extended_helper(b, a)  # pylint: disable=arguments-out-of-order

    exit((c, ac, bc))

exit(_broadcast_dynamic_shape_extended_helper(a, b))
