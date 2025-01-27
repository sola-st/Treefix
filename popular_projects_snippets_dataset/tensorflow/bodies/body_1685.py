# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_test.py
with self.session() as session, self.test_scope():
    data = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11],
                     [12, 13, 14]])
    for dtype in self.all_tf_types:
        for axis in 0, 1, -1:
            params_np = self._buildParams(data, dtype)
            params = array_ops.placeholder(dtype=dtype)
            indices = constant_op.constant(2)
            gather_t = array_ops.gather(params, indices, axis=axis)
            gather_val = session.run(gather_t, feed_dict={params: params_np})
            expected = constant_op.constant(
                np.take(params_np, 2, axis=axis), dtype)
            self.assertAllEqual(expected, gather_val)
