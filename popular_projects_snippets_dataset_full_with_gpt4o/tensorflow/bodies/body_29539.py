# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/edit_distance_op_test.py
hypothesis_indices = [[0, 0, 0], [1, 0, 0]]
hypothesis_values = [0, 1]
hypothesis_shape = [2, 1, 1]
truth_indices = [[0, 1, 0], [1, 0, 0], [1, 1, 0]]
truth_values = [0, 1, 1]
truth_shape = [2, 2, 1]
expected_output = [
    [np.inf, 1.0],  # (0,0): no truth, (0,1): no hypothesis
    [0.0, 1.0]
]  # (1,0): match,    (1,1): no hypothesis

self._testEditDistance(
    hypothesis=(hypothesis_indices, hypothesis_values, hypothesis_shape),
    truth=(truth_indices, truth_values, truth_shape),
    normalize=True,
    expected_output=expected_output)
