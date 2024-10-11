# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
# Test case for GitHub issue:
# https://github.com/tensorflow/tensorflow/issues/45975
value = constant_op.constant(0.0)
with self.assertRaisesRegexp(TypeError,
                             "Cannot convert.*to a TensorFlow DType"):
    check_ops.assert_type(value, (dtypes.float32,))
