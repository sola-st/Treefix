# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session() as sess, self.test_scope():
    dim = array_ops.placeholder(dtypes.int32)
    l = list_ops.empty_tensor_list(
        element_shape=(dim, 15),
        element_dtype=dtypes.float32,
        max_num_elements=20)
    e32 = list_ops.tensor_list_element_shape(l, shape_type=dtypes.int32)
    e64 = list_ops.tensor_list_element_shape(l, shape_type=dtypes.int64)
    self.assertAllEqual(sess.run(e32, {dim: 10}), (10, 15))
    self.assertAllEqual(sess.run(e64, {dim: 7}), (7, 15))
