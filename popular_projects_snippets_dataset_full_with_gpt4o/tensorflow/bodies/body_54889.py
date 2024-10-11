# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
known = tensor_shape.TensorShape([0, 1, 2, 3, 4])
self.assertEqual(tensor_shape.Dimension(2), known[2])
tensor_shape.TensorShape([1, 2, 3]).assert_is_compatible_with(known[1:4])

unknown = tensor_shape.TensorShape(None)
self.assertEqual(
    tensor_shape.Dimension(None).value,
    tensor_shape.dimension_value(unknown[2]))
tensor_shape.TensorShape([None, None,
                          None]).assert_is_compatible_with(unknown[1:4])
