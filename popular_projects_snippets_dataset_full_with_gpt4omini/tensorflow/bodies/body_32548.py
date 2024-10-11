# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
floats = constant_op.constant([1.0, 2.0], name="floats")
with self.assertRaisesRegex(TypeError, "Expected.*integer"):
    check_ops.assert_integer(floats)
