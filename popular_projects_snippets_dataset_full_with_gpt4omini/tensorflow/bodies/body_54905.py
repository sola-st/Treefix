# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
type_1 = tensor_shape.TensorShape([1, None, 3])
self.assertTrue(type_1.is_subtype_of(type_1))
