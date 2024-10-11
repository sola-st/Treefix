# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
type_1 = tensor_shape.TensorShape([None, 2, None])
type_2 = tensor_shape.TensorShape([1, 2, 3])
self.assertNotEqual(type_1, type_2)
self.assertFalse(type_1.is_subtype_of(type_2))
self.assertTrue(type_2.is_subtype_of(type_1))
