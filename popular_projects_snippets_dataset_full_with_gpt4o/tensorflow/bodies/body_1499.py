# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session() as sess, self.test_scope():
    l = list_ops.empty_tensor_list(
        element_shape=(10, 15), element_dtype=dtypes.float32,
        max_num_elements=2)
    l = list_ops.tensor_list_push_back(
        l, array_ops.fill(value=3.0, dims=(10, 15)))
    _, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    self.assertAllEqual(sess.run(e), 3.0 * np.ones((10, 15)))
