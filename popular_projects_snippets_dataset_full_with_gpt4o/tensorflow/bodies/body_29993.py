# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
self.assertEqual(0, self._Zeros([]))
self.assertEqual(0, self._Zeros(()))
scalar = array_ops.zeros(constant_op.constant([], dtype=dtypes_lib.int32))
self.assertEqual(0, scalar.numpy())
