# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
arr = constant_op.constant([1, 5, 2, 2, 3], dtype=dtypes.int32)
ascending = [0, 2, 3, 4, 1]
descending = [1, 4, 2, 3, 0]
with self.cached_session():
    self.assertAllEqual(
        sort_ops.argsort(arr, direction='ASCENDING', stable=True), ascending)
    self.assertAllEqual(
        sort_ops.argsort(arr, direction='DESCENDING', stable=True),
        descending)
