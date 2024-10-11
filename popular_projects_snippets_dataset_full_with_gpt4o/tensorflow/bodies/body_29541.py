# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/edit_distance_op_test.py
hypothesis_indices = [[0, 0]]
hypothesis_values = [0]
hypothesis_shape = [1, 1]
truth_indices = np.empty((0, 2), dtype=np.int64)
truth_values = []
truth_shape = [1, 0]
expected_output = [np.inf]  # Normalized, loss is 1/0 = inf

self._testEditDistance(
    hypothesis=(hypothesis_indices, hypothesis_values, hypothesis_shape),
    truth=(truth_indices, truth_values, truth_shape),
    normalize=True,
    expected_output=expected_output)
