# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bcast_ops_test.py
r0, r1 = self._GetGradientArgs([2, 3, 5], [1])
self.assertAllEqual(r0, [])
self.assertAllEqual(r1, [0, 1, 2])

r0, r1 = self._GetGradientArgs([1], [2, 3, 5])
self.assertAllEqual(r0, [0, 1, 2])
self.assertAllEqual(r1, [])

r0, r1 = self._GetGradientArgs([2, 3, 5], [5])
self.assertAllEqual(r0, [])
self.assertAllEqual(r1, [0, 1])

r0, r1 = self._GetGradientArgs([5], [2, 3, 5])
self.assertAllEqual(r0, [0, 1])
self.assertAllEqual(r1, [])

r0, r1 = self._GetGradientArgs([2, 3, 5], [3, 5])
self.assertAllEqual(r0, [])
self.assertAllEqual(r1, [0])

r0, r1 = self._GetGradientArgs([3, 5], [2, 3, 5])
self.assertAllEqual(r0, [0])
self.assertAllEqual(r1, [])

r0, r1 = self._GetGradientArgs([2, 3, 5], [3, 1])
self.assertAllEqual(r0, [])
self.assertAllEqual(r1, [0, 2])

r0, r1 = self._GetGradientArgs([3, 1], [2, 3, 5])
self.assertAllEqual(r0, [0, 2])
self.assertAllEqual(r1, [])

r0, r1 = self._GetGradientArgs([2, 1, 5], [3, 1])
self.assertAllEqual(r0, [1])
self.assertAllEqual(r1, [0, 2])

r0, r1 = self._GetGradientArgs([3, 1], [2, 1, 5])
self.assertAllEqual(r0, [0, 2])
self.assertAllEqual(r1, [1])
