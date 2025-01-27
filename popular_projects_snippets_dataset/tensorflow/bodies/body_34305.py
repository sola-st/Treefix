# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_from_tensor([1., 2.], element_shape=[])
l = list_ops.tensor_list_resize(l, 4)
self.assertEqual(self.evaluate(list_ops.tensor_list_length(l)), 4)
self.assertEqual(
    self.evaluate(
        list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)),
    1.)
self.assertEqual(
    self.evaluate(
        list_ops.tensor_list_get_item(l, 1, element_dtype=dtypes.float32)),
    2.)
