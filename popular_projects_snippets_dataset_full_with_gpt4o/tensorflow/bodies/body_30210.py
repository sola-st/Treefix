# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
a = array_ops.constant(10)
guarantee_a = array_ops.guarantee_const(a)
self.assertEqual(10, self.evaluate(guarantee_a))
