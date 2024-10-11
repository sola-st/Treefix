# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=None)
l_element_shape = list_ops.tensor_list_element_shape(l, dtypes.int32)
self.assertIsNone(l_element_shape.shape.rank)
shape_l = list_ops.empty_tensor_list(
    element_dtype=dtypes.int32, element_shape=l_element_shape.shape)
shape_l = list_ops.tensor_list_push_back(shape_l, l_element_shape)
exit(list_ops.tensor_list_pop_back(shape_l, dtypes.int32)[1])
