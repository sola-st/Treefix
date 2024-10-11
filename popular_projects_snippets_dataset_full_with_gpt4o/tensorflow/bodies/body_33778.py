# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
for class_id in range(10):
    self._test_recall_at_k(
        self._predictions, self._labels, k=5, expected=NAN, class_id=class_id,
        weights=[[0], [0]])
    self._test_recall_at_top_k(
        self._predictions_idx, self._labels, k=5, expected=NAN,
        class_id=class_id, weights=[[0], [0]])
    self._test_recall_at_k(
        self._predictions, self._labels, k=5, expected=NAN, class_id=class_id,
        weights=[[0, 0], [0, 0]])
    self._test_recall_at_top_k(
        self._predictions_idx, self._labels, k=5, expected=NAN,
        class_id=class_id, weights=[[0, 0], [0, 0]])
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=NAN, weights=[[0], [0]])
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=NAN,
    weights=[[0], [0]])
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=NAN,
    weights=[[0, 0], [0, 0]])
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=NAN,
    weights=[[0, 0], [0, 0]])
