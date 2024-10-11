# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
labels = np.array([
    [[1, 9, 2], [12, 11, 10], [9, 8, 7]],
    [[-5, -5, 7], [6, 5, 4], [3, 2, 1]],
])
predictions = np.array([
    [[4, 8, 12], [1, 2, 3], [4, 5, 6]],
    [[8, 1, 3], [7, 8, 9], [10, 11, 12]],
])
self._test_invalid_weights(
    labels, predictions, weights=np.asarray((1.2, 3.4)))
