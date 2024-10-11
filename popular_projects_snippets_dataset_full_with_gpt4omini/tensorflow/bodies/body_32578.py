# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.assertRaisesRegex(ValueError, regex):
    check_ops.assert_shapes(shapes)
