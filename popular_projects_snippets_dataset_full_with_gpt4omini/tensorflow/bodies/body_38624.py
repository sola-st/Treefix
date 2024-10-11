# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cross_grad_test.py
with self.cached_session():
    us = [2, 3]
    u = array_ops.reshape(
        [0.854, -0.616, 0.767, 0.725, -0.927, 0.159], shape=us)
    v = array_ops.reshape(
        [-0.522, 0.755, 0.407, -0.652, 0.241, 0.247], shape=us)
    s = math_ops.cross(u, v)
    jacob_u, jacob_v = gradient_checker.compute_gradient([u, v], [us, us], s,
                                                         us)

self.assertAllClose(jacob_u[0], jacob_u[1], rtol=1e-3, atol=1e-3)
self.assertAllClose(jacob_v[0], jacob_v[1], rtol=1e-3, atol=1e-3)
