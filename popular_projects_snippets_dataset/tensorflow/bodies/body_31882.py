# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = constant_op.constant([1.2, 3.4], shape=(2, 1))
loss = losses.mean_squared_error(self._labels, self._predictions, weights)
with self.cached_session():
    self.assertAlmostEqual(767.8 / 6.0, self.evaluate(loss), 3)
