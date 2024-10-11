# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_shape=[], num_elements=1, element_dtype=dtypes.float32)
x = constant_op.constant(1.0)
l = list_ops.tensor_list_set_item(l, 0, x)
l_read1 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)
l_read2 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)
grad = gradients_impl.gradients([l_read1, l_read2], [x])
with self.cached_session() as sess:
    self.assertSequenceEqual(self.evaluate(grad), [2.])
