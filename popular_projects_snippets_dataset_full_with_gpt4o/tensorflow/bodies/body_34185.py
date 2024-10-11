# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[2, 3], num_elements=3)
_, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
l = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)
l, e = self.evaluate((l, e))
self.assertAllEqual(e, np.zeros((2, 3)))
self.assertAllEqual(l, np.zeros((3, 2, 3)))
