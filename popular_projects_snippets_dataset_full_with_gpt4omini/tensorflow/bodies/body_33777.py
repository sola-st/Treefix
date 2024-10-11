# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
# Class 2: 4 labels, all correct.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=4.0 / 4, class_id=2)
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=4.0 / 4,
    class_id=2)

# Class 5: 2 labels, both correct.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=2.0 / 2, class_id=5)
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=2.0 / 2,
    class_id=5)

# Class 7: 2 labels, 1 incorrect.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=1.0 / 2, class_id=7)
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=1.0 / 2,
    class_id=7)

# All classes: 12 labels, 7 correct.
self._test_recall_at_k(
    self._predictions, self._labels, k=5, expected=7.0 / 12)
self._test_recall_at_top_k(
    self._predictions_idx, self._labels, k=5, expected=7.0 / 12)
