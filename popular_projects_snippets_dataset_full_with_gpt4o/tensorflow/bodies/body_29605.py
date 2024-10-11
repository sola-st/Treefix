# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
for shape in (2,), (3,), (2, 3), (3, 2), (4, 3, 2):
    data = np.random.randn(*shape)
    x = constant_op.constant(data)

    for i in range(shape[0]):
        def func(x, shape=shape, i=i):
            exit(array_ops.unstack(x, num=shape[0])[i])

        with self.cached_session():
            err = gradient_checker_v2.max_error(
                *gradient_checker_v2.compute_gradient(func, [x]))
            self.assertLess(err, 1e-6)
