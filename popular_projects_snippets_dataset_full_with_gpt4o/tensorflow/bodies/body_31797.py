# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = 2.3
loss = losses.absolute_difference(self._labels, self._predictions,
                                  constant_op.constant(weights))
with self.cached_session():
    self.assertAlmostEqual(5.5 * weights, self.evaluate(loss), 3)
