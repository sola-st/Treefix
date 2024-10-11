# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
expected = (
    np.sum(np.multiply(weights, values)) /
    np.sum(np.multiply(weights, np.ones_like(values)))
)
mean, update_op = metrics.mean(values, weights=weights)
with self.cached_session():
    variables.local_variables_initializer().run()
    self.assertAlmostEqual(expected, self.evaluate(update_op), places=5)
    self.assertAlmostEqual(expected, self.evaluate(mean), places=5)
