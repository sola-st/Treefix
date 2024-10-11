# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
# Classes 0,1 have 0 labels, 0 predictions, classes -1 and 4 are out of
# range.
for labels in self._labels:
    for class_id in (-1, 0, 1, 4):
        self._test_recall_at_k(
            self._predictions, labels, k=1, expected=NAN, class_id=class_id)
        self._test_recall_at_top_k(
            self._predictions_idx, labels, k=1, expected=NAN, class_id=class_id)
