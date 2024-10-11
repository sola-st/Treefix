# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session() as sess, self.test_scope():
    l = list_ops.tensor_list_reserve(
        element_dtype=dtypes.float32,
        element_shape=(7, 15),
        num_elements=2)
    l = list_ops.tensor_list_set_item(
        l, 0, constant_op.constant(1.0, shape=(7, 15)))
    e1 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)
    e2 = list_ops.tensor_list_get_item(l, 1, element_dtype=dtypes.float32)
    self.assertAllEqual(sess.run(e1), np.ones((7, 15)))
    self.assertAllEqual(sess.run(e2), np.zeros((7, 15)))
