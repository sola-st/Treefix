# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = constant_op.constant([3, 6, 5, 0, 4, 2], shape=[2, 3])
loss = losses.absolute_difference(self._labels, self._predictions, weights)
with self.cached_session():
    self.assertAlmostEqual(16.6, self.evaluate(loss), 3)
