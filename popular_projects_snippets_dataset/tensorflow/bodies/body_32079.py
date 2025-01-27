# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
with self.cached_session():
    with self.assertRaisesRegex(ValueError, "Invalid reduction dim"):
        string_ops.reduce_join(inputs="", axis=0)
    with self.assertRaisesRegex(ValueError, "Invalid reduction dimension -3"):
        string_ops.reduce_join(inputs=[[""]], axis=-3)
    with self.assertRaisesRegex(ValueError, "Invalid reduction dimension 2"):
        string_ops.reduce_join(inputs=[[""]], axis=2)
    with self.assertRaisesRegex(ValueError, "Invalid reduction dimension -3"):
        string_ops.reduce_join(inputs=[[""]], axis=[0, -3])
    with self.assertRaisesRegex(ValueError, "Invalid reduction dimension 2"):
        string_ops.reduce_join(inputs=[[""]], axis=[0, 2])
