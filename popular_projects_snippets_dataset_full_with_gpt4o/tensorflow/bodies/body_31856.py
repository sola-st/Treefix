# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = constant_op.constant((1.2, 3.4), shape=(2, 1))
expected_losses = np.multiply(
    self._expected_losses,
    np.asarray([1.2, 1.2, 1.2, 3.4, 3.4, 3.4]).reshape((2, 3)))
loss = losses.log_loss(self._labels, self._predictions, weights)
with self.cached_session():
    self.assertAlmostEqual(-np.sum(expected_losses) / 6.0,
                           self.evaluate(loss), 3)
