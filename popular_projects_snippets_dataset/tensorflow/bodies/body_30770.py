# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bcast_ops_test.py
r0, r1 = self._GetGradientArgs([2, 0, 3, 0, 5], [3, 0, 5])
self.assertAllEqual(r0, [])
self.assertAllEqual(r1, [0, 1])

r0, r1 = self._GetGradientArgs([3, 0, 5], [2, 0, 3, 0, 5])
self.assertAllEqual(r0, [0, 1])
self.assertAllEqual(r1, [])

r0, r1 = self._GetGradientArgs([2, 0, 3, 0, 5], [3, 1, 5])
self.assertAllEqual(r0, [])
self.assertAllEqual(r1, [0, 1, 3])

r0, r1 = self._GetGradientArgs([3, 1, 5], [2, 0, 3, 0, 5])
self.assertAllEqual(r0, [0, 1, 3])
self.assertAllEqual(r1, [])
