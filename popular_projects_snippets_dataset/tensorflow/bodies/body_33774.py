# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
self._predictions = (((0.5, 0.1, 0.6, 0.3, 0.8, 0.0, 0.7, 0.2, 0.4, 0.9),
                      (0.3, 0.0, 0.7, 0.2, 0.4, 0.9, 0.5, 0.8, 0.1, 0.6)),
                     ((0.3, 0.0, 0.7, 0.2, 0.4, 0.9, 0.5, 0.8, 0.1, 0.6),
                      (0.5, 0.1, 0.6, 0.3, 0.8, 0.0, 0.7, 0.2, 0.4, 0.9)))
self._predictions_idx = (((9, 4, 6, 2, 0), (5, 7, 2, 9, 6)),
                         ((5, 7, 2, 9, 6), (9, 4, 6, 2, 0)))
# Note: We don't test dense labels here, since examples have different
# numbers of labels.
self._labels = _binary_3d_label_to_sparse_value(((
    (0, 0, 1, 0, 0, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0, 0, 0, 0)), (
        (0, 1, 1, 0, 0, 1, 0, 1, 0, 0), (0, 0, 1, 0, 0, 0, 0, 0, 1, 0))))
self._test_recall_at_k = functools.partial(
    _test_recall_at_k, test_case=self)
self._test_recall_at_top_k = functools.partial(
    _test_recall_at_top_k, test_case=self)
