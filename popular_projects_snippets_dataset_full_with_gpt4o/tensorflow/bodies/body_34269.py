# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=None)
shape = list_ops.tensor_list_element_shape(l, shape_type=dtypes.int32)
self.assertEqual(self.evaluate(shape), -1)
