# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
"""Tests the case where the numbers of labels differ across examples."""
predictions = [[0.4, 0.3, 0.2, 0.1], [0.1, 0.2, 0.3, 0.4]]
sparse_labels = _binary_2d_label_to_2d_sparse_value(
    [[0, 0, 1, 1], [0, 0, 0, 1]])
dense_labels = np.array([[2, 3], [3, -1]], dtype=np.int64)
predictions_idx_ex1 = np.array(((0, 1, 2, 3), (3, 2, 1, 0)))
precision_ex1 = ((0.0 / 1, 0.0 / 2, 1.0 / 3, 2.0 / 4),
                 (1.0 / 1, 1.0 / 2, 1.0 / 3, 1.0 / 4))
mean_precision_ex1 = np.mean(precision_ex1, axis=0)
avg_precision_ex1 = (
    (0.0 / 1, 0.0 / 2, 1.0 / 3 / 2, (1.0 / 3 + 2.0 / 4) / 2),
    (1.0 / 1, 1.0 / 1, 1.0 / 1, 1.0 / 1))
mean_avg_precision_ex1 = np.mean(avg_precision_ex1, axis=0)
for labels in (sparse_labels, dense_labels):
    for i in range(4):
        k = i + 1
        self._test_precision_at_k(
            predictions, labels, k, expected=mean_precision_ex1[i])
        self._test_precision_at_top_k(
            predictions_idx_ex1[:, :k], labels, k=k,
            expected=mean_precision_ex1[i])
        self._test_average_precision_at_k(
            predictions, labels, k, expected=mean_avg_precision_ex1[i])
