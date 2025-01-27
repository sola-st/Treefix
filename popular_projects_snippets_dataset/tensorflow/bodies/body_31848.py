# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        losses.log_loss(self._labels, self._labels, weights=None)
