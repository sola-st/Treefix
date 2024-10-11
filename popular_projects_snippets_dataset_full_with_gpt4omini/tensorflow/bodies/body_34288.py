# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
t = list_ops.tensor_list_concat(
    l, element_dtype=dtypes.float32, element_shape=(2, 3))
self.assertAllEqual(np.zeros((6, 3)), t)
