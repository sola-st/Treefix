# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    x = ops.convert_to_tensor(tensor_shape.TensorShape([1, 2, 3])[1])
    self.assertEqual(dtypes_lib.int32, x.dtype)
    self.assertAllEqual(2, self.evaluate(x))

    x = ops.convert_to_tensor(
        tensor_shape.TensorShape([1, 2, 3])[1], dtype=dtypes_lib.int64)
    self.assertEqual(dtypes_lib.int64, x.dtype)
    self.assertAllEqual(2, self.evaluate(x))

shape = tensor_shape.TensorShape(None)
if shape._v2_behavior:
    with self.assertRaisesRegex(ValueError, "None values not supported"):
        ops.convert_to_tensor(shape[1])
    with self.assertRaisesRegex(ValueError, "None values not supported"):
        ops.convert_to_tensor(tensor_shape.TensorShape([1, None, 64])[1])
else:
    with self.assertRaisesRegex(ValueError, "unknown Dimension"):
        ops.convert_to_tensor(shape[1])
    with self.assertRaisesRegex(ValueError, "unknown Dimension"):
        ops.convert_to_tensor(tensor_shape.TensorShape([1, None, 64])[1])
