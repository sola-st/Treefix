# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in self.SUPPORTED_DTYPES:
    a = constant_op.constant([1, 2, 3, 4, 5, 6], shape=[2, 3], dtype=dtype)
    b = constant_op.constant([7, 8, 9, 10, 11, 12], shape=[3, 2], dtype=dtype)
    c = math_ops.matmul(a, b)
    c_np = constant_op.constant([[58, 64], [139, 154]],
                                shape=(2, 2),
                                dtype=dtype)
    self.assertAllClose(c, c_np, atol=1e-2)
