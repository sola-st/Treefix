# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
for dtype in [np.float32, np.float64]:
    g = ops.Graph()
    with g.as_default():
        mu = variables.Variable(dtype(0.0))
        sigma = variables.Variable(dtype(1.0))
        dist = normal_lib.Normal(loc=mu, scale=sigma)
        x = np.array([-100., -20., -5., 0., 5., 20., 100.]).astype(dtype)
        for func in [
            dist.cdf, dist.log_cdf, dist.survival_function,
            dist.log_survival_function, dist.log_prob, dist.prob
        ]:
            value = func(x)
            grads = gradients_impl.gradients(value, [mu, sigma])
            with self.session(graph=g):
                self.evaluate(variables.global_variables_initializer())
                self.assertAllFinite(value)
                self.assertAllFinite(grads[0])
                self.assertAllFinite(grads[1])
