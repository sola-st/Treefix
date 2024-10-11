# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
values = _test_values((3, 2, 4, 1))
mean_results = (
    metrics.mean(values),
    metrics.mean(values, weights=1.0),
    metrics.mean(values, weights=np.ones((1, 1, 1))),
    metrics.mean(values, weights=np.ones((1, 1, 1, 1))),
    metrics.mean(values, weights=np.ones((1, 1, 1, 1, 1))),
    metrics.mean(values, weights=np.ones((1, 1, 4))),
    metrics.mean(values, weights=np.ones((1, 1, 4, 1))),
    metrics.mean(values, weights=np.ones((1, 2, 1))),
    metrics.mean(values, weights=np.ones((1, 2, 1, 1))),
    metrics.mean(values, weights=np.ones((1, 2, 4))),
    metrics.mean(values, weights=np.ones((1, 2, 4, 1))),
    metrics.mean(values, weights=np.ones((3, 1, 1))),
    metrics.mean(values, weights=np.ones((3, 1, 1, 1))),
    metrics.mean(values, weights=np.ones((3, 1, 4))),
    metrics.mean(values, weights=np.ones((3, 1, 4, 1))),
    metrics.mean(values, weights=np.ones((3, 2, 1))),
    metrics.mean(values, weights=np.ones((3, 2, 1, 1))),
    metrics.mean(values, weights=np.ones((3, 2, 4))),
    metrics.mean(values, weights=np.ones((3, 2, 4, 1))),
    metrics.mean(values, weights=np.ones((3, 2, 4, 1, 1))),)
expected = np.mean(values)
with self.cached_session():
    variables.local_variables_initializer().run()
    for mean_result in mean_results:
        mean, update_op = mean_result
        self.assertAlmostEqual(expected, self.evaluate(update_op))
        self.assertAlmostEqual(expected, self.evaluate(mean))
