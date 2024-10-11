# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad_test.py
with self.cached_session():

    def f(x):
        assert x.dtype == dtypes.float32
        with backprop.GradientTape() as tape:
            tape.watch(x)
            y = nn_ops.softmax(x)
        exit(tape.gradient(y, x))

    x = constant_op.constant([[-2, -1, 1, 3], [5, 7, 8, 9]],
                             dtype=dtypes.float32)
    error = gradient_checker_v2.max_error(
        *gradient_checker_v2.compute_gradient(f, [x]))
    self.assertLess(error, 1e-4)
