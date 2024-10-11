# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
tf_predictions = array_ops.placeholder(dtypes.float32, shape=[None, None])
weights = 2.3
loss = losses.log_loss(self._labels, tf_predictions,
                       constant_op.constant(weights))
with self.cached_session() as sess:
    loss = sess.run(loss, feed_dict={tf_predictions: self._np_predictions})
    self.assertAlmostEqual(weights * -np.sum(self._expected_losses) / 6.0,
                           loss, 3)
