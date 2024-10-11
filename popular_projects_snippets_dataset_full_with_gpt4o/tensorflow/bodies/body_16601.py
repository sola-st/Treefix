# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
arr = np.random.random((5, 6, 7, 8))
for axis in range(4):
    with self.cached_session():
        self.assertAllEqual(
            np.argsort(arr, axis=axis), sort_ops.argsort(arr, axis=axis))
