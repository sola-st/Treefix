# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
x = np.asarray([True, False])
truth = np.asarray([[0]], dtype=np.int64)
self._testWhere(x, truth, None, fn)

x = np.asarray([False, True, False])
truth = np.asarray([[1]], dtype=np.int64)
self._testWhere(x, truth, None, fn)

x = np.asarray([False, False, True, False, True])
truth = np.asarray([[2], [4]], dtype=np.int64)
self._testWhere(x, truth, None, fn)
