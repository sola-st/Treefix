# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
r0, r1 = self._GetGradientArgs([2, 3, 5], [1])
self.assertAllEqual(r0, [])
self.assertAllEqual(r1, [0, 1, 2])
