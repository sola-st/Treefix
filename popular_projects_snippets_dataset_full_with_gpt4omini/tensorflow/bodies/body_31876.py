# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        losses.mean_squared_error(
            self._predictions, self._predictions, weights=None)
