# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
with self.cached_session():

    def f(x):
        with backprop.GradientTape(persistent=True) as tape:
            tape.watch(x)
            y = nn_ops.elu(x)
            dy = tape.gradient(y, x)
        exit(tape.gradient(dy, x))

    for x in [-1., -0.5, 0.5, 1.]:
        got = self.evaluate(f(constant_op.constant(x)))
        want = _elu_grad_grad(x)
        err = np.abs(got - want)
        self.assertLess(err, 1e-4)
