# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_test.py
with self.session() as session, self.test_scope():
    data = np.array([[0, 0, 0, 0], [0, 2 * (1 + np.exp2(-8)), 0, 0],
                     [0, 0, 0, 0], [0.015789, 0.0985, 0.55789, 0.3842]])
    indices = np.array([1, 2, 3, 1])
    dtype = dtypes.float32
    params_np = self._buildParams(data, dtype)
    params = array_ops.placeholder(dtype=dtype)
    indices_tf = constant_op.constant(indices)
    gather_t = array_ops.gather(params, indices_tf)
    gather_val = session.run(gather_t, feed_dict={params: params_np})
    np_val = params_np[indices]
    self.assertAllEqual(np_val, gather_val)
