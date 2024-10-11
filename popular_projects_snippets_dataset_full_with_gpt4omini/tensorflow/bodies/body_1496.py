# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session() as sess, self.test_scope():
    val = array_ops.placeholder(dtype=dtypes.float32)
    l = list_ops.empty_tensor_list(
        element_shape=(7, 15),
        element_dtype=dtypes.float32,
        max_num_elements=10)
    # Note: Pushing a Placeholder will force the constant folding code
    # to build a Const node with a DT_VARIANT output. This tests that XLA
    # passes a cf_consider_fn which prevent folding such nodes.
    l = list_ops.tensor_list_push_back(
        l, array_ops.fill(value=val, dims=(7, 15)))
    l = list_ops.tensor_list_push_back(
        l, constant_op.constant(2.0, shape=(7, 15)))
    l, e2 = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    _, e1 = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    self.assertAllEqual(sess.run(e2, {val: 1.0}), 2.0 * np.ones((7, 15)))
    self.assertAllEqual(sess.run(e1, {val: 1.0}), 1.0 * np.ones((7, 15)))
