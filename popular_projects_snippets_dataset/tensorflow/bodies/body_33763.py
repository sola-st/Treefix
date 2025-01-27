# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
self._predictions = ((0.1, 0.3, 0.2, 0.4), (0.1, 0.2, 0.3, 0.4))
self._predictions_idx = [[3], [3]]
indicator_labels = ((0, 0, 0, 1), (0, 0, 1, 0))
class_labels = (3, 2)
# Sparse vs dense, and 1d vs 2d labels should all be handled the same.
self._labels = (
    _binary_2d_label_to_1d_sparse_value(indicator_labels),
    _binary_2d_label_to_2d_sparse_value(indicator_labels), np.array(
        class_labels, dtype=np.int64), np.array(
            [[class_id] for class_id in class_labels], dtype=np.int64))
self._test_recall_at_k = functools.partial(
    _test_recall_at_k, test_case=self)
self._test_recall_at_top_k = functools.partial(
    _test_recall_at_top_k, test_case=self)
