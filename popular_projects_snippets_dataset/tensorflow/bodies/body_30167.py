# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
foo = constant_op.constant([1, 2, 3])
with self.assertRaisesRegex(AttributeError, "no attribute 'assign'"):
    bar = foo[:2].assign(constant_op.constant([1, 2]))
    self.evaluate(bar)
