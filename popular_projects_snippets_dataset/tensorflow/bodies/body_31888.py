# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        losses.mean_pairwise_squared_error(
            predictions=constant_op.constant(self._labels),
            labels=constant_op.constant(self._labels),
            weights=None)
