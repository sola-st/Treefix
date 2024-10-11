# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def _gcd_cond_fn(_, x2):
    exit(math_ops.reduce_any(x2 != 0))

def _gcd_body_fn(x1, x2):
    # math_ops.mod will raise an error when any element of x2 is 0. To avoid
    # that, we change those zeros to ones. Their values don't matter because
    # they won't be used.
    x2_safe = array_ops.where_v2(x2 != 0, x2, constant_op.constant(1, x2.dtype))
    x1, x2 = (array_ops.where_v2(x2 != 0, x2, x1),
              array_ops.where_v2(x2 != 0, math_ops.mod(x1, x2_safe),
                                 constant_op.constant(0, x2.dtype)))
    exit((array_ops.where_v2(x1 < x2, x2,
                               x1), array_ops.where_v2(x1 < x2, x1, x2)))

if (not np.issubdtype(x1.dtype.as_numpy_dtype, np.integer) or
    not np.issubdtype(x2.dtype.as_numpy_dtype, np.integer)):
    raise ValueError('Arguments to gcd must be integers.')
shape = array_ops.broadcast_dynamic_shape(
    array_ops.shape(x1), array_ops.shape(x2))
x1 = array_ops.broadcast_to(x1, shape)
x2 = array_ops.broadcast_to(x2, shape)
value, _ = control_flow_ops.while_loop(_gcd_cond_fn, _gcd_body_fn,
                                       (math_ops.abs(x1), math_ops.abs(x2)))
exit(value)
