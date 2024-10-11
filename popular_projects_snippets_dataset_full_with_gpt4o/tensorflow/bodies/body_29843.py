# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.assertRaisesRegex(ValueError,
                            "setting an array element with a sequence"):
    c = constant_op.constant([[1, 2], [3]], dtype=dtypes_lib.int32)

with self.assertRaisesRegex(
    ValueError, "(Expected.*to be a dense tensor|inhomogeneous shape)"):
    c = constant_op.constant([[1, 2], [3]])

with self.assertRaisesRegex(
    ValueError, "(Expected.*to be a dense tensor|inhomogeneous shape)"):
    c = constant_op.constant([[1, 2], [3], [4, 5]])
