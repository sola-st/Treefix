# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
with self.session():
    for dtype in (dtypes.bfloat16, dtypes.float16, dtypes.float32,
                  dtypes.float64):
        # A large number is needed to get Eigen to die
        x = array_ops.zeros((0, 9938), dtype=dtype)
        y = math_ops.reduce_mean(x, [0]).eval()
        self.assertEqual(y.shape, (9938,))
        self.assertTrue(np.all(np.isnan(y)))
