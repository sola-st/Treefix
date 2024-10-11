# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/edit_distance_op_test.py
hypothesis_indices = [[0, 0], [1, 0], [1, 1]]
hypothesis_values = [10, 10, 11]
hypothesis_shape = [2, 2]
truth_indices = [[0, 0], [0, 1], [1, 0], [1, 1]]
truth_values = [1, 2, 1, -1]
truth_shape = [2, 3]
expected_output = [2.0, 2.0]

self._testEditDistance(
    hypothesis=(hypothesis_indices, hypothesis_values, hypothesis_shape),
    truth=(truth_indices, truth_values, truth_shape),
    normalize=False,
    expected_output=expected_output)
