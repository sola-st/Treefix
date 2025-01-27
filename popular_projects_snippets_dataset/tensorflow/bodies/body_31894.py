# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = 2.3
loss = losses.mean_pairwise_squared_error(
    predictions=constant_op.constant(self._predictions),
    labels=constant_op.constant(self._labels),
    weights=constant_op.constant(weights))
with self.cached_session():
    self.assertAlmostEqual(weights * np.sum(self._expected_losses),
                           self.evaluate(loss), 3)
