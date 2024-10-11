# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=[])
e0 = constant_op.constant(5.)
l = list_ops.tensor_list_set_item(
    l, 0, 2. * e0, resize_if_index_out_of_bounds=True)
l = list_ops.tensor_list_set_item(
    l, 1, 1., resize_if_index_out_of_bounds=True)
t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)
grad = gradients_impl.gradients(t, e0)[0]
self.assertAllEqual(self.evaluate(grad), 2.)
