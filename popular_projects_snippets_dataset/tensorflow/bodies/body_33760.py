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

# Class 2: 2 predictions, both correct.
self._test_precision_at_k(
    predictions, labels, k=5, expected=2.0 / 2.0, class_id=2,
    weights=[[1], [0]])
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=2.0 / 2.0, class_id=2,
    weights=[[1], [0]])

# Class 2: 2 predictions, both correct.
self._test_precision_at_k(
    predictions, labels, k=5, expected=2.0 / 2.0, class_id=2,
    weights=[[0], [1]])
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=2.0 / 2.0, class_id=2,
    weights=[[0], [1]])

# Class 7: 1 incorrect prediction.
self._test_precision_at_k(
    predictions, labels, k=5, expected=0.0 / 1.0, class_id=7,
    weights=[[1], [0]])
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=0.0 / 1.0, class_id=7,
    weights=[[1], [0]])

# Class 7: 1 correct prediction.
self._test_precision_at_k(
    predictions, labels, k=5, expected=1.0 / 1.0, class_id=7,
    weights=[[0], [1]])
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=1.0 / 1.0, class_id=7,
    weights=[[0], [1]])

# Class 7: no predictions.
self._test_precision_at_k(
    predictions, labels, k=5, expected=NAN, class_id=7,
    weights=[[1, 0], [0, 1]])
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=NAN, class_id=7,
    weights=[[1, 0], [0, 1]])

# Class 7: 2 predictions, 1 correct.
self._test_precision_at_k(
    predictions, labels, k=5, expected=1.0 / 2.0, class_id=7,
    weights=[[0, 1], [1, 0]])
self._test_precision_at_top_k(
    predictions_idx, labels, k=5, expected=1.0 / 2.0, class_id=7,
    weights=[[0, 1], [1, 0]])
