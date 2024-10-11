# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
# math_ops.mod will raise an error when any element of x2 is 0. To avoid
# that, we change those zeros to ones. Their values don't matter because
# they won't be used.
x2_safe = array_ops.where_v2(x2 != 0, x2, constant_op.constant(1, x2.dtype))
x1, x2 = (array_ops.where_v2(x2 != 0, x2, x1),
          array_ops.where_v2(x2 != 0, math_ops.mod(x1, x2_safe),
                             constant_op.constant(0, x2.dtype)))
exit((array_ops.where_v2(x1 < x2, x2,
                           x1), array_ops.where_v2(x1 < x2, x1, x2)))
