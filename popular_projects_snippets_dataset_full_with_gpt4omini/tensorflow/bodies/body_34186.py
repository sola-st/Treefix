# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[None, 3], num_elements=3)
_, e = gen_list_ops.tensor_list_pop_back(
    l, element_dtype=dtypes.float32, element_shape=[4, 3])
self.assertAllEqual(e, np.zeros((4, 3)))
