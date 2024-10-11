# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
arr = np.random.random((10, 5, 5))
with self.cached_session():
    self.assertAllEqual(
        np.sort(arr, axis=0)[::-1],
        sort_ops.sort(
            constant_op.constant(arr), axis=0, direction='DESCENDING'))
