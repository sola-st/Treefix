# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
# Example 1.
# Matches example here:
# fastml.com/what-you-wanted-to-know-about-mean-average-precision
labels_ex1 = (0, 1, 2, 3, 4)
labels = np.array([labels_ex1], dtype=np.int64)
predictions_ex1 = (0.2, 0.1, 0.0, 0.4, 0.0, 0.5, 0.3)
predictions = (predictions_ex1,)
predictions_idx_ex1 = (5, 3, 6, 0, 1)
precision_ex1 = (0.0 / 1, 1.0 / 2, 1.0 / 3, 2.0 / 4)
avg_precision_ex1 = (0.0 / 1, precision_ex1[1] / 2, precision_ex1[1] / 3,
                     (precision_ex1[1] + precision_ex1[3]) / 4)
for i in range(4):
    k = i + 1
    self._test_precision_at_k(
        predictions, labels, k, expected=precision_ex1[i])
    self._test_precision_at_top_k(
        (predictions_idx_ex1[:k],), labels, k=k, expected=precision_ex1[i])
    self._test_average_precision_at_k(
        predictions, labels, k, expected=avg_precision_ex1[i])

# Example 2.
labels_ex2 = (0, 2, 4, 5, 6)
labels = np.array([labels_ex2], dtype=np.int64)
predictions_ex2 = (0.3, 0.5, 0.0, 0.4, 0.0, 0.1, 0.2)
predictions = (predictions_ex2,)
predictions_idx_ex2 = (1, 3, 0, 6, 5)
precision_ex2 = (0.0 / 1, 0.0 / 2, 1.0 / 3, 2.0 / 4)
avg_precision_ex2 = (0.0 / 1, 0.0 / 2, precision_ex2[2] / 3,
                     (precision_ex2[2] + precision_ex2[3]) / 4)
for i in range(4):
    k = i + 1
    self._test_precision_at_k(
        predictions, labels, k, expected=precision_ex2[i])
    self._test_precision_at_top_k(
        (predictions_idx_ex2[:k],), labels, k=k, expected=precision_ex2[i])
    self._test_average_precision_at_k(
        predictions, labels, k, expected=avg_precision_ex2[i])

# Both examples, we expect both precision and average precision to be the
# average of the 2 examples.
labels = np.array([labels_ex1, labels_ex2], dtype=np.int64)
predictions = (predictions_ex1, predictions_ex2)
streaming_precision = [(ex1 + ex2) / 2
                       for ex1, ex2 in zip(precision_ex1, precision_ex2)]
streaming_average_precision = [
    (ex1 + ex2) / 2
    for ex1, ex2 in zip(avg_precision_ex1, avg_precision_ex2)
]
for i in range(4):
    k = i + 1
    predictions_idx = (predictions_idx_ex1[:k], predictions_idx_ex2[:k])
    self._test_precision_at_k(
        predictions, labels, k, expected=streaming_precision[i])
    self._test_precision_at_top_k(
        predictions_idx, labels, k=k, expected=streaming_precision[i])
    self._test_average_precision_at_k(
        predictions, labels, k, expected=streaming_average_precision[i])

# Weighted examples, we expect streaming average precision to be the
# weighted average of the 2 examples.
weights = (0.3, 0.6)
streaming_average_precision = [
    (weights[0] * ex1 + weights[1] * ex2) / (weights[0] + weights[1])
    for ex1, ex2 in zip(avg_precision_ex1, avg_precision_ex2)
]
for i in range(4):
    k = i + 1
    self._test_average_precision_at_k(
        predictions,
        labels,
        k,
        expected=streaming_average_precision[i],
        weights=weights)
