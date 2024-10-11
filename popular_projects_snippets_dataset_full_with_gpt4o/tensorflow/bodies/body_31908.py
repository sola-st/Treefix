# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
loss = losses.cosine_distance(
    predictions=constant_op.constant(self._predictions),
    labels=constant_op.constant(self._labels),
    dim=2,
    weights=np.asarray((1, 0, 0)).reshape((3, 1, 1)))
with self.cached_session():
    self.assertEqual(1.0, self.evaluate(loss))
