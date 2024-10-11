# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    x = ops.convert_to_tensor(tensor_shape.TensorShape([]))
    self.assertEqual(dtypes_lib.int32, x.dtype)
    self.assertAllEqual([], self.evaluate(x))

    x = ops.convert_to_tensor(tensor_shape.TensorShape([1, 2, 3]))
    self.assertEqual(dtypes_lib.int32, x.dtype)
    self.assertAllEqual([1, 2, 3], self.evaluate(x))

    x = ops.convert_to_tensor(tensor_shape.TensorShape([2**31-1, 2, 3]))
    self.assertEqual(dtypes_lib.int32, x.dtype)
    self.assertAllEqual([2**31 - 1, 2, 3], self.evaluate(x))

    x = ops.convert_to_tensor(tensor_shape.TensorShape([2**31-1, 2, 3]),
                              dtype=dtypes_lib.int32)
    self.assertEqual(dtypes_lib.int32, x.dtype)
    self.assertAllEqual([2**31 - 1, 2, 3], self.evaluate(x))

    x = ops.convert_to_tensor(tensor_shape.TensorShape([2**31, 2, 3]))
    self.assertEqual(dtypes_lib.int64, x.dtype)
    self.assertAllEqual([2**31, 2, 3], self.evaluate(x))

    x = ops.convert_to_tensor(tensor_shape.TensorShape([2**31, 2, 3]),
                              dtype=dtypes_lib.int64)
    self.assertEqual(dtypes_lib.int64, x.dtype)
    self.assertAllEqual([2**31, 2, 3], self.evaluate(x))

    with self.assertRaisesRegex(ValueError,
                                "a dimension is too large.*int64"):
        x = ops.convert_to_tensor(tensor_shape.TensorShape([2**31, 2, 3]),
                                  dtype=dtypes_lib.int32)

    x = ops.convert_to_tensor(
        tensor_shape.TensorShape([1, 2, 3]), dtype=dtypes_lib.int64)
    self.assertEqual(dtypes_lib.int64, x.dtype)
    self.assertAllEqual([1, 2, 3], self.evaluate(x))

    x = array_ops.reshape(
        array_ops.zeros([6]), tensor_shape.TensorShape([2, 3]))
    self.assertAllEqual([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], self.evaluate(x))

with self.assertRaisesRegex(ValueError, "partially known"):
    ops.convert_to_tensor(tensor_shape.TensorShape(None))

with self.assertRaisesRegex(ValueError, "partially known"):
    ops.convert_to_tensor(tensor_shape.TensorShape([1, None, 64]))

with self.assertRaises(TypeError):
    ops.convert_to_tensor(
        tensor_shape.TensorShape([1, 2, 3]), dtype=dtypes_lib.float32)
