# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session(), self.test_scope():
    t = constant_op.constant([1.0, 2.0])
    l = list_ops.tensor_list_from_tensor(t, element_shape=[])
    e0 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)
    self.assertAllEqual(e0, 1.0)
    l = list_ops.tensor_list_set_item(l, 0, 3.0)
    t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)
    self.assertAllEqual(t, [3.0, 2.0])
