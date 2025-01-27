# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
# Classes 0,3,4,6,9 have 0 labels, class 10 is out of range.
for class_id in (0, 3, 4, 6, 9, 10):
    self._test_recall_at_k(
        self._predictions, self._labels, k=5, expected=NAN, class_id=class_id)
    self._test_recall_at_top_k(
        self._predictions_idx, self._labels, k=5, expected=NAN,
        class_id=class_id)
