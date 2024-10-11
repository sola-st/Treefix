# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = array_ops.zeros((2, 3))
loss = losses.absolute_difference(self._labels, self._predictions, weights)
with self.cached_session():
    self.assertAlmostEqual(0.0, self.evaluate(loss), 3)
