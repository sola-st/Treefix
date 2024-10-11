# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in self.SUPPORTED_DTYPES:
    a = constant_op.constant(np.arange(1, 13), shape=[2, 2, 3], dtype=dtype)
    b = constant_op.constant(np.arange(13, 25), shape=[2, 3, 2], dtype=dtype)
    c = math_ops.matmul(a, b)
    c_np = constant_op.constant(
        [[[94, 100], [229, 244]], [[508, 532], [697, 730]]],
        shape=[2, 2, 2],
        dtype=dtype)
    self.assertAllClose(c, c_np, atol=1e-2)
