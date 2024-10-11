# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
self._compareExpandDimsAll(np.zeros([2]), 0)
self._compareExpandDimsAll(np.zeros([2]), 1)
self._compareExpandDimsAll(np.zeros([2]), -1)

self._compareExpandDimsAll(np.zeros([2, 3]), 0)
self._compareExpandDimsAll(np.zeros([2, 3]), 1)
self._compareExpandDimsAll(np.zeros([2, 3]), 2)
self._compareExpandDimsAll(np.zeros([2, 3]), -1)
self._compareExpandDimsAll(np.zeros([2, 3]), -2)

self._compareExpandDimsAll(np.zeros([2, 3, 5]), 0)
self._compareExpandDimsAll(np.zeros([2, 3, 5]), 1)
self._compareExpandDimsAll(np.zeros([2, 3, 5]), 2)
self._compareExpandDimsAll(np.zeros([2, 3, 5]), 3)

self._compareExpandDimsAll(np.zeros([2, 3, 5]), -1)
self._compareExpandDimsAll(np.zeros([2, 3, 5]), -2)
self._compareExpandDimsAll(np.zeros([2, 3, 5]), -3)
self._compareExpandDimsAll(np.zeros([2, 3, 5]), -4)
