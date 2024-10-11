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

# Classes 1,3,8 have 0 predictions, classes -1 and 10 are out of range.
for class_id in (-1, 1, 3, 8, 10):
    self._test_precision_at_k(
        predictions, labels, k=5, expected=NAN, class_id=class_id)
    self._test_precision_at_top_k(
        predictions_idx, labels, k=5, expected=NAN, class_id=class_id)
