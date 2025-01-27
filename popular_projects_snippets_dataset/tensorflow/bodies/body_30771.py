# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bcast_ops_test.py
for dtype in [dtypes.int32, dtypes.int64]:
    r = self._GetBroadcastShape(
        constant_op.constant([2, 3, 5], dtype=dtype),
        constant_op.constant([1], dtype=dtype))
    self.assertAllEqual(r, [2, 3, 5])

    r0, r1 = self._GetGradientArgs(
        constant_op.constant([2, 3, 5], dtype=dtype),
        constant_op.constant([1], dtype=dtype))
    self.assertAllEqual(r0, [])
    self.assertAllEqual(r1, [0, 1, 2])
