# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = [[0.5, 0.1, 0.6, 0.3, 0.8, 0.0, 0.7, 0.2, 0.4, 0.9],
               [0.3, 0.0, 0.7, 0.2, 0.4, 0.9, 0.5, 0.8, 0.1, 0.6]]
predictions_idx = [[9, 4, 6, 2, 0], [5, 7, 2, 9, 6]]
sparse_labels = _binary_2d_label_to_2d_sparse_value(
    [[0, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 0, 0, 0, 0]])
dense_labels = np.array([[2, 7, 8], [1, 2, 5]], dtype=np.int64)

for labels in (sparse_labels, dense_labels):
    # Class 2: 2 labels, 2 correct predictions.
    self._test_precision_at_k(
        predictions, labels, k=5, expected=2.0 / 2, class_id=2)
    self._test_precision_at_top_k(
        predictions_idx, labels, k=5, expected=2.0 / 2, class_id=2)

    # Class 5: 1 label, 1 correct prediction.
    self._test_precision_at_k(
        predictions, labels, k=5, expected=1.0 / 1, class_id=5)
    self._test_precision_at_top_k(
        predictions_idx, labels, k=5, expected=1.0 / 1, class_id=5)

    # Class 7: 1 label, 1 incorrect prediction.
    self._test_precision_at_k(
        predictions, labels, k=5, expected=0.0 / 1, class_id=7)
    self._test_precision_at_top_k(
        predictions_idx, labels, k=5, expected=0.0 / 1, class_id=7)

    # All classes: 10 predictions, 3 correct.
    self._test_precision_at_k(
        predictions, labels, k=5, expected=3.0 / 10)
    self._test_precision_at_top_k(
        predictions_idx, labels, k=5, expected=3.0 / 10)
