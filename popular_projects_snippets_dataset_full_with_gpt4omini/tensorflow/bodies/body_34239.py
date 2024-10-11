# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[], num_elements=3)
l = list_ops.tensor_list_set_item(l, 0, 5.)
e1 = list_ops.tensor_list_get_item(l, 1, element_dtype=dtypes.float32)
e2 = list_ops.tensor_list_get_item(l, 2, element_dtype=dtypes.float32)
self.assertEqual(self.evaluate(e1), 0.)
self.assertEqual(self.evaluate(e2), 0.)
