# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
keys = np.array([[2, 4, 1, 3], [3, 1, 4, 2]], dtype=np.float32)
c = self._NewComputation()
ops.Sort(c, [ops.Constant(c, keys)], is_stable=True)
self._ExecuteAndCompareClose(
    c,
    expected=[np.array([[1, 2, 3, 4], [1, 2, 3, 4]], dtype=np.float32)])
