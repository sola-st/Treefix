# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bcast_ops_test.py
r = self._GetBroadcastShape([2, 3, 5], [1])
self.assertAllEqual(r, [2, 3, 5])

r = self._GetBroadcastShape([1], [2, 3, 5])
self.assertAllEqual(r, [2, 3, 5])

r = self._GetBroadcastShape([2, 3, 5], [5])
self.assertAllEqual(r, [2, 3, 5])

r = self._GetBroadcastShape([5], [2, 3, 5])
self.assertAllEqual(r, [2, 3, 5])

r = self._GetBroadcastShape([2, 3, 5], [3, 5])
self.assertAllEqual(r, [2, 3, 5])

r = self._GetBroadcastShape([3, 5], [2, 3, 5])
self.assertAllEqual(r, [2, 3, 5])

r = self._GetBroadcastShape([2, 3, 5], [3, 1])
self.assertAllEqual(r, [2, 3, 5])

r = self._GetBroadcastShape([3, 1], [2, 3, 5])
self.assertAllEqual(r, [2, 3, 5])

r = self._GetBroadcastShape([2, 1, 5], [3, 1])
self.assertAllEqual(r, [2, 3, 5])

r = self._GetBroadcastShape([3, 1], [2, 1, 5])
self.assertAllEqual(r, [2, 3, 5])
