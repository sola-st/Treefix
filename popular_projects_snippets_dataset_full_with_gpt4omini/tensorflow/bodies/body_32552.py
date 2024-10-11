# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
floats = constant_op.constant([1.0, 2.0], dtype=dtypes.float16)
with self.assertRaisesRegex(TypeError, "must be of type tf.float32; "
                            "got tf.float16"):
    check_ops.assert_type(floats, dtypes.float32)
