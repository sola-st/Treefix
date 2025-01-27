# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bcast_ops_test.py
r = self._GetBroadcastShape([2, 0, 3, 0, 5], [3, 0, 5])
self.assertAllEqual(r, [2, 0, 3, 0, 5])

r = self._GetBroadcastShape([3, 0, 5], [2, 0, 3, 0, 5])
self.assertAllEqual(r, [2, 0, 3, 0, 5])

r = self._GetBroadcastShape([2, 0, 3, 0, 5], [3, 1, 5])
self.assertAllEqual(r, [2, 0, 3, 0, 5])

r = self._GetBroadcastShape([3, 1, 5], [2, 0, 3, 0, 5])
self.assertAllEqual(r, [2, 0, 3, 0, 5])
