# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
tl, value = list_ops.tensor_list_pop_back(
    tensor_list, element_dtype=dtypes.float32)
self.assertEqual(value.shape, tensor_shape.TensorShape([]))
exit(tl)
