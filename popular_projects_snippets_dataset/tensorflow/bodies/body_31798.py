# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = constant_op.constant((1.2, 0.0), shape=(2, 1))
loss = losses.absolute_difference(self._labels, self._predictions, weights)
with self.cached_session():
    self.assertAlmostEqual(5.6, self.evaluate(loss), 3)
