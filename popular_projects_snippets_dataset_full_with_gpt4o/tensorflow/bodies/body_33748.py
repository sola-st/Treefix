# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
for labels in self._labels:
    # Class 3: 1 label, 2 predictions, 1 correct.
    self._test_precision_at_k(
        self._predictions, labels, k=1, expected=1.0 / 2, class_id=3)
    self._test_precision_at_top_k(
        self._predictions_idx, labels, k=1, expected=1.0 / 2, class_id=3)

    # All classes: 2 labels, 2 predictions, 1 correct.
    self._test_precision_at_k(
        self._predictions, labels, k=1, expected=1.0 / 2)
    self._test_precision_at_top_k(
        self._predictions_idx, labels, k=1, expected=1.0 / 2)
    self._test_average_precision_at_k(
        self._predictions, labels, k=1, expected=1.0 / 2)
