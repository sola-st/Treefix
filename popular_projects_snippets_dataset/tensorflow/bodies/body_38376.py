# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
with self.session():
    for dtype in (dtypes.bfloat16, dtypes.float16, dtypes.float32,
                  dtypes.float64, dtypes.complex64, dtypes.complex128):
        # A large number is needed to get Eigen to die
        x = array_ops.zeros((0, 9938), dtype=dtype)
        y = math_ops.reduce_sum(x, [0])
        self.assertAllEqual(y, np.zeros(9938))
