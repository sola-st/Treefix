# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session() as sess, self.test_scope():
    l = list_ops.empty_tensor_list(
        element_shape=[],
        element_dtype=dtypes.float32,
        max_num_elements=20)
    l = list_ops.tensor_list_push_back(l, constant_op.constant(1.0))
    l2 = list_ops.tensor_list_push_back(l, constant_op.constant(2.0))
    l3 = list_ops.tensor_list_push_back(l, constant_op.constant(3.0))
    _, e11 = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    l2, e21 = list_ops.tensor_list_pop_back(l2, element_dtype=dtypes.float32)
    l2, e22 = list_ops.tensor_list_pop_back(l2, element_dtype=dtypes.float32)
    l3, e31 = list_ops.tensor_list_pop_back(l3, element_dtype=dtypes.float32)
    l3, e32 = list_ops.tensor_list_pop_back(l3, element_dtype=dtypes.float32)
    result = sess.run([e11, [e21, e22], [e31, e32]])
    self.assertEqual(result, [1.0, [2.0, 1.0], [3.0, 1.0]])
