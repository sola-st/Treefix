# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = np.array([0, 0, 0, 0, 0, 2]).reshape((2, 3))
expected_losses = np.multiply(self._expected_losses, weights)

loss = losses.log_loss(
    self._labels,
    self._predictions,
    constant_op.constant(
        weights, shape=(2, 3)))
with self.cached_session():
    self.assertAlmostEqual(-np.sum(expected_losses), self.evaluate(loss), 3)
