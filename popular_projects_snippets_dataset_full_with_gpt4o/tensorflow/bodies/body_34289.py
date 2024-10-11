# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
t, _ = gen_list_ops.tensor_list_concat_v2(
    l,
    element_dtype=dtypes.float32,
    element_shape=list_ops._build_element_shape((None, 3)),
    leading_dims=[2, 3, 5])
self.assertAllEqual(np.zeros((10, 3)), t)
l = list_ops.tensor_list_set_item(l, 1, [[2., 3.], [4., 5.], [6., 7.]])
t, _ = gen_list_ops.tensor_list_concat_v2(
    l,
    element_dtype=dtypes.float32,
    element_shape=list_ops._build_element_shape((None, 2)),
    leading_dims=[2, 3, 4])
self.assertAllEqual([[0., 0.], [0., 0.], [2., 3.], [4., 5.], [6., 7.],
                     [0., 0.], [0., 0.], [0., 0.], [0., 0.]], t)
