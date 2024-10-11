# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
dtype = np.float32
degree = 3
shapes = [(1,), (2, 1), (1, 2), (2, 2)]
for x_shape in shapes:
    for coeff_shape in shapes:
        with self.subTest(x_shape=x_shape, coeff_shape=coeff_shape):
            x = np.random.rand(*x_shape).astype(dtype)
            coeffs = [
                np.random.rand(*coeff_shape).astype(dtype)
                for _ in range(degree + 1)
            ]
            np_val = np.polyval(coeffs, x)
            with self.cached_session():
                tf_val = math_ops.polyval(coeffs, x)
                self.assertAllClose(np_val, self.evaluate(tf_val))
