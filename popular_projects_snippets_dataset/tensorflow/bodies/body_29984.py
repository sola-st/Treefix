# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
with self.assertRaisesRegex(ValueError, "non-rectangular Python sequence"):
    constant_op.constant([[1, 2], [3]], dtype=dtypes_lib.int32)

with self.assertRaisesRegex(ValueError, None):
    constant_op.constant([[1, 2], [3]])

with self.assertRaisesRegex(ValueError, None):
    constant_op.constant([[1, 2], [3], [4, 5]])
