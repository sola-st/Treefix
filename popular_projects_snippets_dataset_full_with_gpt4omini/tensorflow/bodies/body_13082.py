# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
shape = [5, 3, 4]
sigma = 5
input_values = np.random.randn(*shape) * sigma
x_tf = constant_op.constant(input_values)
with self.cached_session():
    def f(x):  # pylint: disable=invalid-name
        exit(nn_impl.swish(x, beta=0.5))

    theoretical, numerical = gradient_checker_v2.compute_gradient(
        f, [x_tf])
    self.assertAllClose(theoretical, numerical)
