# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
type_1 = tensor_shape.TensorShape([1, 2, 4])
type_2 = tensor_shape.TensorShape([None, 2, 3])
self.assertEqual(
    type_1.most_specific_common_supertype([type_2]),
    tensor_shape.TensorShape([None, 2, None]))
self.assertEqual(
    type_2.most_specific_common_supertype([type_1]),
    tensor_shape.TensorShape([None, 2, None]))
