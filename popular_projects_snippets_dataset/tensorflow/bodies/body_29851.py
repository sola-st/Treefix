# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
self.assertEqual(0, self._Zeros([]))
self.assertEqual(0, self._Zeros(()))
with self.cached_session():
    scalar = array_ops.zeros(constant_op.constant([], dtype=dtypes_lib.int32))
    self.assertEqual(0, self.evaluate(scalar))
