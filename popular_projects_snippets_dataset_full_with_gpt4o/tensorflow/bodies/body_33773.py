# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
"""Tests that labels outside the [0, n_classes) count in denominator."""
labels = sparse_tensor.SparseTensorValue(
    indices=[[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2],
             [1, 3]],
    # values -1 and 10 are outside the [0, n_classes) range.
    values=np.array([2, 7, -1, 8, 1, 2, 5, 10], np.int64),
    dense_shape=[2, 4])

# Class 2: 2 labels, both correct.
self._test_recall_at_k(
    self._predictions, labels, k=5, expected=2.0 / 2, class_id=2)
self._test_recall_at_top_k(
    self._predictions_idx, labels, k=5, expected=2.0 / 2, class_id=2)

# Class 5: 1 label, incorrect.
self._test_recall_at_k(
    self._predictions, labels, k=5, expected=1.0 / 1, class_id=5)
self._test_recall_at_top_k(
    self._predictions_idx, labels, k=5, expected=1.0 / 1, class_id=5)

# Class 7: 1 label, incorrect.
self._test_recall_at_k(
    self._predictions, labels, k=5, expected=0.0 / 1, class_id=7)
self._test_recall_at_top_k(
    self._predictions_idx, labels, k=5, expected=0.0 / 1, class_id=7)

# All classes: 8 labels, 3 correct.
self._test_recall_at_k(self._predictions, labels, k=5, expected=3.0 / 8)
self._test_recall_at_top_k(
    self._predictions_idx, labels, k=5, expected=3.0 / 8)
