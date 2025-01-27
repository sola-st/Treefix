# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
for labels in self._labels:
    # Class 8: 1 label, no predictions.
    self._test_recall_at_k(
        self._predictions, labels, k=5, expected=0.0 / 1, class_id=8)
    self._test_recall_at_top_k(
        self._predictions_idx, labels, k=5, expected=0.0 / 1, class_id=8)
