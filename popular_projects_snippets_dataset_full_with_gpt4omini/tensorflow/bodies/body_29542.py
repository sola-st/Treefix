# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/edit_distance_op_test.py
hypothesis_indices = np.empty((0, 2), dtype=np.int64)
hypothesis_values = []
hypothesis_shape = [1, 0]
truth_indices = np.empty((0, 2), dtype=np.int64)
truth_values = []
truth_shape = [1, 0]
expected_output = [0]  # Normalized is 0 because of exact match

self._testEditDistance(
    hypothesis=(hypothesis_indices, hypothesis_values, hypothesis_shape),
    truth=(truth_indices, truth_values, truth_shape),
    normalize=True,
    expected_output=expected_output)
