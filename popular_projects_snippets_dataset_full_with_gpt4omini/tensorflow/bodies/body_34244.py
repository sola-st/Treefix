# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=None)
l = list_ops.tensor_list_push_back(l, constant_op.constant(1.0))
l = list_ops.tensor_list_push_back(l, constant_op.constant([1.0, 2.0]))
l, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(e), [1.0, 2.0])
l, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(e), 1.0)
