# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
loss = losses.cosine_distance(
    predictions=constant_op.constant(self._predictions),
    labels=constant_op.constant(self._labels),
    dim=2,
    weights=array_ops.zeros((3, 1, 1)))
with self.cached_session():
    self.assertEqual(0, self.evaluate(loss))
