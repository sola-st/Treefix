# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
a = constant_op.constant(np.arange(1, 13), shape=[2, 2, 3], dtype=a_dtype)
b = constant_op.constant(np.arange(13, 25), shape=[2, 3, 2], dtype=b_dtype)
c_np = constant_op.constant(
    [[[94, 100], [229, 244]], [[508, 532], [697, 730]]],
    shape=[2, 2, 2],
    dtype=dtypes.int32)
c = math_ops.matmul(a, b, output_type=dtypes.int32)
self.assertAllEqual(c, c_np)
