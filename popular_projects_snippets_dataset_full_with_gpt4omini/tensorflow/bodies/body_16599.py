# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
arr = np.random.random(42)
with self.cached_session():
    self.assertAllEqual(
        np.sort(arr), array_ops.gather(arr, sort_ops.argsort(arr)))
