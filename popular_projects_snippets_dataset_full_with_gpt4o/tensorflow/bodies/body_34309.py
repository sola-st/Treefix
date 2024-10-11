# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
t = constant_op.constant([1., 2., 3.])
l = list_ops.tensor_list_from_tensor(t, element_shape=[])
l = list_ops.tensor_list_set_item(
    l, 3, 4., resize_if_index_out_of_bounds=True)
t1 = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)
grad = gradients_impl.gradients(t1, t)[0]
self.assertAllEqual(self.evaluate(grad), [1., 1., 1.])
