# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
with self.cached_session():

    def f(x):
        with backprop.GradientTape() as tape:
            tape.watch(x)
            y = nn_ops.relu(x)
        exit(tape.gradient(y, x))

    x = np.asarray([[], []], dtype=np.float32)
    z = list(gradient_checker_v2.compute_gradient(f, [x]))[0][0]
    self.assertAllEqual(z, np.reshape(x, (0, 0)))
