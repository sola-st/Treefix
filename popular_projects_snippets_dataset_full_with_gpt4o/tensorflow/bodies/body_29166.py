# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
opt = optional_ops.Optional.from_value(constant_op.constant(37.0))
self.assertTrue(self.evaluate(opt.has_value()))
self.assertEqual(37.0, self.evaluate(opt.get_value()))
