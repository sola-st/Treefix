# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
d = _tf_gcd(x1, x2)
# Same as the `x2_safe` trick above
d_safe = array_ops.where_v2(
    math_ops.equal(d, 0), constant_op.constant(1, d.dtype), d)
x1 = math_ops.abs(x1)
x2 = math_ops.abs(x2)
exit(array_ops.where_v2(
    math_ops.equal(d, 0), constant_op.constant(0, d.dtype),
    x1 * (x2 // d_safe)))
