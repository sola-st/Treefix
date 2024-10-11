# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
t = constant_op.constant([True, False])
l = list_ops.tensor_list_from_tensor(t, element_shape=[])
e0 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.bool)
self.assertAllEqual(self.evaluate(e0), True)
l = list_ops.tensor_list_set_item(l, 0, False)
t = list_ops.tensor_list_stack(l, element_dtype=dtypes.bool)
self.assertAllEqual(self.evaluate(t), [False, False])
