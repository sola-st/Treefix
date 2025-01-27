# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
l = list_ops.tensor_list_set_item(l, 1, [[2., 3.], [4., 5.], [6., 7.]])
t = list_ops.tensor_list_concat(l, element_dtype=dtypes.float32)
self.assertAllEqual([[0., 0.], [0., 0.], [0., 0.], [2., 3.], [4., 5.],
                     [6., 7.], [0., 0.], [0., 0.], [0., 0.]], t)
