# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
five = tensor_shape.TensorShape([5])
result = addend + five
self.assertIsInstance(result, tensor_shape.TensorShape)
tensor_shape.TensorShape([2, 3, 4, 5]).assert_is_compatible_with(result)
