# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = constant_op.constant(np.random.normal(size=(2, 4)), shape=[2, 4])
with self.cached_session():
    with self.assertRaises(ValueError):
        losses.log_loss(self._labels, self._predictions, weights)
