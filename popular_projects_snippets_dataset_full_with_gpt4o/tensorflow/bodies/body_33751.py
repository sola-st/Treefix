# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
"""Tests that labels outside the [0, n_classes) range are ignored."""
labels_ex1 = (-1, 0, 1, 2, 3, 4, 7)
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
