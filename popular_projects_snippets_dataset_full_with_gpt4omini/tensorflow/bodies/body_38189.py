# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x_ = ops.convert_to_tensor(x)
epsilon = 1e-3
with self.cached_session():
    for args in [(x_, 0.), (0., x_)]:
        with self.subTest(args=args):
            z = math_ops.reduce_sum(math_ops.abs(math_ops.complex(*args)))
            jacob_t, jacob_n = gradient_checker.compute_gradient(
                x_, list(x.shape), z, [1], x_init_value=x, delta=epsilon)
            self.assertAllClose(jacob_t, jacob_n, rtol=epsilon, atol=epsilon)
