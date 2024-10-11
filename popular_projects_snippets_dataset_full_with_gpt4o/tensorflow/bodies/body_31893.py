# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weight = 2.3
self._test_valid_weights(
    self._labels, self._predictions,
    expected_loss=weight * np.sum(self._expected_losses),
    weights=weight)
