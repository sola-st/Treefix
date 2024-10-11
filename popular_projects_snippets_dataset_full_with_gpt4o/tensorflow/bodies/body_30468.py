# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/fingerprint_op_test.py
f0 = self.evaluate(array_ops.fingerprint([]))
self.assertEqual(f0.ndim, 2)
self.assertEqual(f0.shape, (0, 8))
