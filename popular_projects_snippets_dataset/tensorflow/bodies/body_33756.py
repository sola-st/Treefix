# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
"""Tests that labels outside the [0, n_classes) range are ignored."""
predictions = [[0.5, 0.1, 0.6, 0.3, 0.8, 0.0, 0.7, 0.2, 0.4, 0.9],
               [0.3, 0.0, 0.7, 0.2, 0.4, 0.9, 0.5, 0.8, 0.1, 0.6]]
predictions_idx = [[9, 4, 6, 2, 0], [5, 7, 2, 9, 6]]
sp_labels = sparse_tensor.SparseTensorValue(
    indices=[[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2],
             [1, 3]],
    # values -1 and 10 are outside the [0, n_classes) range and are ignored.
    values=np.array([2, 7, -1, 8, 1, 2, 5, 10], np.int64),
    dense_shape=[2, 4])

# Class 2: 2 labels, 2 correct predictions.
self._test_precision_at_k(
    predictions, sp_labels, k=5, expected=2.0 / 2, class_id=2)
self._test_precision_at_top_k(
    predictions_idx, sp_labels, k=5, expected=2.0 / 2, class_id=2)

# Class 5: 1 label, 1 correct prediction.
self._test_precision_at_k(
    predictions, sp_labels, k=5, expected=1.0 / 1, class_id=5)
self._test_precision_at_top_k(
    predictions_idx, sp_labels, k=5, expected=1.0 / 1, class_id=5)

# Class 7: 1 label, 1 incorrect prediction.
self._test_precision_at_k(
    predictions, sp_labels, k=5, expected=0.0 / 1, class_id=7)
self._test_precision_at_top_k(
    predictions_idx, sp_labels, k=5, expected=0.0 / 1, class_id=7)

# All classes: 10 predictions, 3 correct.
self._test_precision_at_k(
    predictions, sp_labels, k=5, expected=3.0 / 10)
self._test_precision_at_top_k(
    predictions_idx, sp_labels, k=5, expected=3.0 / 10)
