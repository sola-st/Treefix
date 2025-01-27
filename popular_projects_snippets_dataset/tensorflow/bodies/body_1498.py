# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session() as sess, self.test_scope():
    l = list_ops.empty_tensor_list(
        element_shape=(7, 15), element_dtype=dtypes.float32)
    l = list_ops.tensor_list_push_back(
        l, constant_op.constant(1.0, shape=(7, 15)))
    _, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "Set the max number of elements"):
        self.assertAllEqual(sess.run(e), 1.0 * np.ones((7, 15)))
