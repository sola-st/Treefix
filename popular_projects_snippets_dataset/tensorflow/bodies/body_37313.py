# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
x = np.arange(1, 9).reshape(shape).astype(np.float64)
with self.cached_session():
    t = ops.convert_to_tensor(x)
    result = math_ops.cumprod(t, axis, exclusive, reverse)
    jacob_t, jacob_n = gradient_checker.compute_gradient(
        t, shape, result, shape, x_init_value=x, delta=1)
self.assertAllClose(jacob_t, jacob_n, rtol=1e-8, atol=1e-8)
