# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
loss = losses.absolute_difference(self._predictions, self._predictions)
with self.cached_session():
    self.assertAlmostEqual(0.0, self.evaluate(loss), 3)
