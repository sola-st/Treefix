# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
for labels in self._labels:
    # Class 2: 0 predictions.
    self._test_recall_at_k(
        self._predictions, labels, k=1, expected=0.0, class_id=2)
    self._test_recall_at_top_k(
        self._predictions_idx, labels, k=1, expected=0.0, class_id=2)
