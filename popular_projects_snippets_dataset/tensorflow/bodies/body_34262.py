# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.cached_session() as sess:
    ph = array_ops.placeholder(dtypes.float32)
    c = constant_op.constant([1.0, 2.0])
    l = list_ops.tensor_list_from_tensor(c, element_shape=[])
    # Set a placeholder with unknown shape to satisfy the shape inference
    # at graph building time.
    l = list_ops.tensor_list_set_item(l, 0, ph)
    l_0 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "incompatible shape"):
        sess.run(l_0, {ph: [3.0]})
