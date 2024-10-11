# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
x_val = np.random.random_sample(x_shape).astype(np.float32)
np_c, np_m, np_v, np_s = self._npSuffStats(x_val, axes, shift, keep_dims)
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu) as sess:
        if has_shape:
            x = constant_op.constant(x_val, name="x")
            x.set_shape(x_shape)
            op_c, op_m, op_v, op_s = self._opSuffStats(x, axes, shift, keep_dims)
            if shift:
                tf_c, tf_m, tf_v, tf_s = self.evaluate([op_c, op_m, op_v, op_s])
            else:
                tf_c, tf_m, tf_v = self.evaluate([op_c, op_m, op_v])
        else:
            x = array_ops.placeholder(
                dtype=dtypes.float32, shape=[None] * len(x_shape), name="x")
            op_c, op_m, op_v, op_s = self._opSuffStats(x, axes, shift, keep_dims)
            if shift:
                tf_c, tf_m, tf_v, tf_s = sess.run([op_c, op_m, op_v, op_s],
                                                  feed_dict={x: x_val})
            else:
                tf_c, tf_m, tf_v = sess.run([op_c, op_m, op_v],
                                            feed_dict={x: x_val})
        self.assertAllClose(np_c, tf_c, atol=0.000001)
        self.assertAllClose(np_m, tf_m, atol=0.000001)
        self.assertAllClose(np_v, tf_v, atol=0.000001)
        if shift:
            self.assertAllClose(np_s, tf_s, atol=0.000001)
