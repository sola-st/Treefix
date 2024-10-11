# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32,
    element_shape=[],
    max_num_elements=max_num_elements)
l = list_ops.tensor_list_push_back(l, constant_op.constant(1.0))
l, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
l = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)
l, e = self.evaluate((l, e))
self.assertAllEqual(l, [])
self.assertAllEqual(e, 1.0)
