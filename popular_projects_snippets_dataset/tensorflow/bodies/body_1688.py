# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_test.py
"""Check that scalar and empty indices shapes work as well."""
shape = (2, 1, 3, 2)
for indices_shape in (), (0,), (2, 0), (2, 3):
    for dtype in self.all_tf_types:
        for axis in 0, 1, 2, 3, -1, -2:
            params = self._buildParams(np.random.randn(*shape), dtype)
            indices = np.random.randint(shape[axis], size=indices_shape)
            with self.session() as sess, self.test_scope():
                tf_params = array_ops.placeholder(dtype=dtype)
                tf_indices = constant_op.constant(indices, dtype=dtypes.int32)
                gather = array_ops.gather(tf_params, tf_indices, axis=axis)
                gather_value = sess.run(gather, feed_dict={tf_params: params})
                gather_np = constant_op.constant(
                    np.take(params, indices, axis=axis), dtype)
                self.assertAllEqual(gather_np, gather_value)
