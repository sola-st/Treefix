# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
loss = losses.log_loss(self._labels, self._predictions)
with self.cached_session():
    self.assertAlmostEqual(-np.sum(self._expected_losses) / 6.0,
                           self.evaluate(loss), 3)
