# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
val = ops.convert_to_tensor(b"\0\0\0\0").numpy()
self.assertEqual(len(val), 4)
self.assertEqual(val, b"\0\0\0\0")

val = ops.convert_to_tensor(b"xx\0xx").numpy()
self.assertEqual(len(val), 5)
self.assertAllEqual(val, b"xx\0xx")

nested = [[b"\0\0\0\0", b"xx\0xx"], [b"\0_\0_\0_\0", b"\0"]]
val = ops.convert_to_tensor(nested).numpy()
# NOTE(mrry): Do not use assertAllEqual, because it converts nested to a
#   numpy array, which loses the null terminators.
self.assertEqual(val.tolist(), nested)
