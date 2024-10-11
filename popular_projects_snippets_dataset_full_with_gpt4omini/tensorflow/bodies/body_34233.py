# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
t = constant_op.constant([1.0, 2.0], dtype=dtype)
l = list_ops.tensor_list_from_tensor(t, element_shape=[])
e0 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtype)
self.assertAllEqual(self.evaluate(e0), 1.0)
l = list_ops.tensor_list_set_item(
    l, 0, constant_op.constant(3.0, dtype=dtype))
t = list_ops.tensor_list_stack(l, element_dtype=dtype)
self.assertAllEqual(self.evaluate(t), [3.0, 2.0])
