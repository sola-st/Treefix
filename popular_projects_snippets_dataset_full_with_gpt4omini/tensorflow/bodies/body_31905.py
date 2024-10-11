# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
loss = losses.cosine_distance(
    predictions=constant_op.constant(self._labels),
    labels=constant_op.constant(self._labels),
    dim=2)
with self.cached_session():
    self.assertAlmostEqual(0, self.evaluate(loss), 5)
