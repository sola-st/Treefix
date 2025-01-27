# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session(), self.test_scope():
    t = constant_op.constant([1.0, 2.0])
    l = list_ops.tensor_list_from_tensor(t, element_shape=[])
    e = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)
    self.assertAllEqual(e, 1.0)
    l, e0 = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    self.assertAllEqual(e0, 2.0)
    l, e1 = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    self.assertAllEqual(e1, 1.0)
    self.assertAllEqual(list_ops.tensor_list_length(l), 2)
