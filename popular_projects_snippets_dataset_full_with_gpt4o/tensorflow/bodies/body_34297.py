# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_split([1., 2., 3., 4., 5],
                               element_shape=None,
                               lengths=[3, 2])
self.assertAllEqual(list_ops.tensor_list_length(l), 2)
self.assertAllEqual(
    list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32),
    [1., 2., 3.])
self.assertAllEqual(
    list_ops.tensor_list_get_item(l, 1, element_dtype=dtypes.float32),
    [4., 5.])
