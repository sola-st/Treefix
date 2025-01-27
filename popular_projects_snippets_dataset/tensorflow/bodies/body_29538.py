# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/edit_distance_op_test.py
# In this case, the values are individual characters stored in the
# SparseTensor (type DT_STRING)
hypothesis_indices = ([[0, i] for i, _ in enumerate("algorithm")] +
                      [[1, i] for i, _ in enumerate("altruistic")])
hypothesis_values = [x for x in "algorithm"] + [x for x in "altruistic"]
hypothesis_shape = [2, 11]
truth_indices = ([[0, i] for i, _ in enumerate("altruistic")] +
                 [[1, i] for i, _ in enumerate("algorithm")])
truth_values = [x for x in "altruistic"] + [x for x in "algorithm"]
truth_shape = [2, 11]
expected_unnormalized = [6.0, 6.0]
expected_normalized = [6.0 / len("altruistic"), 6.0 / len("algorithm")]

self._testEditDistance(
    hypothesis=(hypothesis_indices, hypothesis_values, hypothesis_shape),
    truth=(truth_indices, truth_values, truth_shape),
    normalize=False,
    expected_output=expected_unnormalized)

self._testEditDistance(
    hypothesis=(hypothesis_indices, hypothesis_values, hypothesis_shape),
    truth=(truth_indices, truth_values, truth_shape),
    normalize=True,
    expected_output=expected_normalized)
