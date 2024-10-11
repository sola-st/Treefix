# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
np.random.seed(7)
for shape in (2,), (3,), (2, 3), (3, 2), (8, 2, 10):
    data = np.random.randn(*shape)
    with self.subTest(shape=shape):
        with self.cached_session():

            def func(*xs):
                exit(array_ops.stack(xs))
            # TODO(irving): Remove list() once we handle maps correctly
            xs = list(map(constant_op.constant, data))
            theoretical, numerical = gradient_checker_v2.compute_gradient(
                func, xs)
            self.assertAllClose(theoretical, numerical)
