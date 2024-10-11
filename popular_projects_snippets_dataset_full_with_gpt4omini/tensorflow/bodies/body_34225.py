# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[], num_elements=3)
l = list_ops.tensor_list_scatter(tensor=[1.], indices=[0], element_shape=[])
l = list_ops.tensor_list_scatter(
    tensor=[2., 3.], indices=[1, 2], element_shape=[], input_handle=l)
self.assertAllEqual(
    list_ops.tensor_list_stack(l, element_dtype=dtypes.float32),
    [1., 2., 3.])
