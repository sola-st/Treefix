# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
s = [2, 3, 4, 2]
x = np.arange(1.0, 49.0).reshape(s).astype(np.float64)
with self.cached_session():
    t = ops.convert_to_tensor(x)
    su = math_ops.reduce_min(t, [1, 2])
    jacob_t, jacob_n = gradient_checker.compute_gradient(
        t, s, su, [2, 2], x_init_value=x, delta=1)
self.assertAllClose(jacob_t, jacob_n, rtol=1e-8, atol=1e-8)
