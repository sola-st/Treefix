# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
g = ops.Graph()
with g.as_default():
    mu = variables.Variable(dtype(0.0))
    sigma = variables.Variable(dtype(1.0))
    dist = normal_lib.Normal(loc=mu, scale=sigma)
    p = variables.Variable(
        np.array([0.,
                  np.exp(-32.), np.exp(-2.),
                  1. - np.exp(-2.), 1. - np.exp(-32.),
                  1.]).astype(dtype))

    value = dist.quantile(p)
    grads = gradients_impl.gradients(value, [mu, p])
    with self.cached_session(graph=g):
        self.evaluate(variables.global_variables_initializer())
        self.assertAllFinite(grads[0])
        self.assertAllFinite(grads[1])
