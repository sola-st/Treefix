# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = self._predictions
predictions_idx = self._predictions_idx
for labels in self._labels:
    # Class 3: 1 label, 2 predictions, 1 correct.
    self._test_recall_at_k(
        predictions, labels, k=1, expected=NAN, class_id=3, weights=(0.0,))
    self._test_recall_at_top_k(
        predictions_idx, labels, k=1, expected=NAN, class_id=3,
        weights=(0.0,))
    self._test_recall_at_k(
        predictions, labels, k=1, expected=1.0 / 1, class_id=3,
        weights=(1.0,))
    self._test_recall_at_top_k(
        predictions_idx, labels, k=1, expected=1.0 / 1, class_id=3,
        weights=(1.0,))
    self._test_recall_at_k(
        predictions, labels, k=1, expected=1.0 / 1, class_id=3,
        weights=(2.0,))
    self._test_recall_at_top_k(
        predictions_idx, labels, k=1, expected=1.0 / 1, class_id=3,
        weights=(2.0,))
    self._test_recall_at_k(
        predictions, labels, k=1, expected=NAN, class_id=3,
        weights=(0.0, 1.0))
    self._test_recall_at_top_k(
        predictions_idx, labels, k=1, expected=NAN, class_id=3,
        weights=(0.0, 1.0))
    self._test_recall_at_k(
        predictions, labels, k=1, expected=1.0 / 1, class_id=3,
        weights=(1.0, 0.0))
    self._test_recall_at_top_k(
        predictions_idx, labels, k=1, expected=1.0 / 1, class_id=3,
        weights=(1.0, 0.0))
    self._test_recall_at_k(
        predictions, labels, k=1, expected=2.0 / 2, class_id=3,
        weights=(2.0, 3.0))
    self._test_recall_at_top_k(
        predictions_idx, labels, k=1, expected=2.0 / 2, class_id=3,
        weights=(2.0, 3.0))
