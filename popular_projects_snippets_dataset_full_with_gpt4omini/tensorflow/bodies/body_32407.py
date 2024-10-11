# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor = constant_op.constant(1)
with self.assertRaisesRegex(TypeError, "proper"):
    check_ops.assert_proper_iterable(tensor)
