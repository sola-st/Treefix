# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
l = list_ops.tensor_list_set_item(l, 1, [1., 2.])
t = list_ops.tensor_list_gather(l, [1, 2], element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(t), [[1., 2.], [0., 0.]])
