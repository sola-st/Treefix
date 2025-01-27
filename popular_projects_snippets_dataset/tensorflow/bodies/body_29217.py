# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/convert_test.py
self.assertAllEqual([-1],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            tensor_shape.TensorShape([None]))))
self.assertAllEqual([-1],
                    self.evaluate(convert.partial_shape_to_tensor((None,))))
self.assertAllEqual([-1],
                    self.evaluate(convert.partial_shape_to_tensor([None])))
self.assertAllEqual([-1],
                    self.evaluate(convert.partial_shape_to_tensor([-1])))
self.assertAllEqual([-1],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            constant_op.constant([-1],
                                                 dtype=dtypes.int64))))

with self.assertRaisesRegex(
    ValueError, r"The given shape .* must be a 1-D tensor of `tf.int64` "
    r"values, but the shape was \(2, 2\)."):
    convert.partial_shape_to_tensor(constant_op.constant(
        [[1, 1], [1, 1]], dtype=dtypes.int64))

with self.assertRaisesRegex(
    TypeError, r"The given shape .* must be a 1-D tensor of `tf.int64` "
    r"values, but the element type was float32."):
    convert.partial_shape_to_tensor(constant_op.constant([1., 1.]))
