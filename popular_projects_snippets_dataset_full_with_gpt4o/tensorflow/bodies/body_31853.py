# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = 2.3
loss = losses.log_loss(self._labels, self._predictions,
                       constant_op.constant(weights))
with self.cached_session():
    self.assertAlmostEqual(weights * -np.sum(self._expected_losses) / 6.0,
                           self.evaluate(loss), 3)
