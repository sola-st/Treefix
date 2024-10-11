# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = [[[0.5, 0.1, 0.6, 0.3, 0.8, 0.0, 0.7, 0.2, 0.4, 0.9],
                [0.3, 0.0, 0.7, 0.2, 0.4, 0.9, 0.5, 0.8, 0.1, 0.6]],
               [[0.3, 0.0, 0.7, 0.2, 0.4, 0.9, 0.5, 0.8, 0.1, 0.6],
                [0.5, 0.1, 0.6, 0.3, 0.8, 0.0, 0.7, 0.2, 0.4, 0.9]]]
predictions_idx = [[[9, 4, 6, 2, 0], [5, 7, 2, 9, 6]],
                   [[5, 7, 2, 9, 6], [9, 4, 6, 2, 0]]]
labels = _binary_3d_label_to_sparse_value(
    [[[0, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 0, 0, 0, 0]],
     [[0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]]])

# Class 2: 4 predictions, all correct.
self._test_precision_at_k(
    predictions, labels, k=5, expected=4.0 / 4, class_id=2)
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=4.0 / 4, class_id=2)

# Class 5: 2 predictions, both correct.
self._test_precision_at_k(
    predictions, labels, k=5, expected=2.0 / 2, class_id=5)
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=2.0 / 2, class_id=5)

# Class 7: 2 predictions, 1 correct.
self._test_precision_at_k(
    predictions, labels, k=5, expected=1.0 / 2, class_id=7)
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=1.0 / 2, class_id=7)

# All classes: 20 predictions, 7 correct.
self._test_precision_at_k(
    predictions, labels, k=5, expected=7.0 / 20)
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=7.0 / 20)
