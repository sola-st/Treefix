# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
tf_weights = array_ops.zeros(shape=(2, 3))
loss = losses.log_loss(self._labels, self._predictions, tf_weights)
with self.cached_session():
    self.assertAlmostEqual(0.0, self.evaluate(loss), 3)
