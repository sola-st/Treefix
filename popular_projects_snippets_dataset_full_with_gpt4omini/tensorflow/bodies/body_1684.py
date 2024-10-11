# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_test.py
with self.session() as session, self.test_scope():
    data = np.array([0, 1, 2, 3, 7, 5])
    for dtype in self.all_tf_types:
        for indices in 4, [4], [1, 2, 2, 4, 5]:
            params_np = self._buildParams(data, dtype)
            params = array_ops.placeholder(dtype=dtype)
            indices_tf = constant_op.constant(indices)
            gather_t = array_ops.gather(params, indices_tf)
            gather_val = session.run(gather_t, feed_dict={params: params_np})
            np_val = constant_op.constant(params_np[indices])
            self.assertAllEqual(np_val, gather_val)
