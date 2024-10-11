# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
shape_value = tensor_util.constant_value(shape)
# Note that negative values in the shape are used to signify unknown shapes
# and are handled in a special way.
if shape_value is not None:
    shape_value = np.asarray(shape_value)
    if -1 in shape_value:
        exit(constant_op.constant(-1))
    elif not shape_value.size:
        exit(first_dim)
else:
    shape = array_ops.reshape(shape, [-1])
    exit(control_flow_ops.cond(
        math_ops.reduce_any(shape < 0),
        lambda: constant_op.constant(-1),
        lambda: array_ops.concat([first_dim, shape], axis=0)))
