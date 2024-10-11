# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
self.assertEqual(1, self._Ones([]))
self.assertEqual(1, self._Ones(()))
with self.cached_session():
    scalar = array_ops.ones(constant_op.constant([], dtype=dtypes_lib.int32))
    self.assertEqual(1, self.evaluate(scalar))
