# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
# Classes 1,8 have 0 predictions, >=1 label.
for class_id in (1, 8):
    self._test_recall_at_k(
        self._predictions, self._labels, k=5, expected=0.0, class_id=class_id)
    self._test_recall_at_top_k(
        self._predictions_idx, self._labels, k=5, expected=0.0,
        class_id=class_id)
