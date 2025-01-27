# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
for labels in self._labels:
    # Class 2: 2 labels, both correct.
    self._test_recall_at_k(
        self._predictions, labels, k=5, expected=2.0 / 2, class_id=2)
    self._test_recall_at_top_k(
        self._predictions_idx, labels, k=5, expected=2.0 / 2, class_id=2)

    # Class 5: 1 label, incorrect.
    self._test_recall_at_k(
        self._predictions, labels, k=5, expected=1.0 / 1, class_id=5)
    self._test_recall_at_top_k(
        self._predictions_idx, labels, k=5, expected=1.0 / 1, class_id=5)

    # Class 7: 1 label, incorrect.
    self._test_recall_at_k(
        self._predictions, labels, k=5, expected=0.0 / 1, class_id=7)
    self._test_recall_at_top_k(
        self._predictions_idx, labels, k=5, expected=0.0 / 1, class_id=7)

    # All classes: 6 labels, 3 correct.
    self._test_recall_at_k(self._predictions, labels, k=5, expected=3.0 / 6)
    self._test_recall_at_top_k(
        self._predictions_idx, labels, k=5, expected=3.0 / 6)
