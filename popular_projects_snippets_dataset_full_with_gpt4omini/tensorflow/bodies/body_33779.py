# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
# Class 2: 2 labels, both correct.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=2.0 / 2.0, class_id=2,
    weights=[[1], [0]])
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=2.0 / 2.0,
    class_id=2, weights=[[1], [0]])

# Class 2: 2 labels, both correct.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=2.0 / 2.0, class_id=2,
    weights=[[0], [1]])
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=2.0 / 2.0,
    class_id=2, weights=[[0], [1]])

# Class 7: 1 label, correct.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=1.0 / 1.0, class_id=7,
    weights=[[0], [1]])
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=1.0 / 1.0,
    class_id=7, weights=[[0], [1]])

# Class 7: 1 label, incorrect.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=0.0 / 1.0, class_id=7,
    weights=[[1], [0]])
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=0.0 / 1.0,
    class_id=7, weights=[[1], [0]])

# Class 7: 2 labels, 1 correct.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=1.0 / 2.0, class_id=7,
    weights=[[1, 0], [1, 0]])
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=1.0 / 2.0,
    class_id=7, weights=[[1, 0], [1, 0]])

# Class 7: No labels.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=NAN, class_id=7,
    weights=[[0, 1], [0, 1]])
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=NAN, class_id=7,
    weights=[[0, 1], [0, 1]])
