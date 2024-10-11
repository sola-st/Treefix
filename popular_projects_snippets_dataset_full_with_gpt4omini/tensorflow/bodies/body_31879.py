# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
loss = losses.mean_squared_error(self._labels, self._predictions)
with self.cached_session():
    self.assertAlmostEqual(49.5, self.evaluate(loss), 3)
