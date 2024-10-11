# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = ragged_factory_ops.constant([[1, 2], [3]])
with self.assertRaisesRegex(TypeError, "must be of type.*float32"):
    check_ops.assert_type(x, dtypes.float32)
