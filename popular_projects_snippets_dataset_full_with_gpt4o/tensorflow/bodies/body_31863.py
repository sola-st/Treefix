# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = np.array([0, 0, 0, 0, 0, 2]).reshape((2, 3))
expected_losses = np.multiply(self._expected_losses, weights)

tf_predictions = array_ops.placeholder(dtypes.float32, shape=[2, 3])
tf_weights = constant_op.constant(weights, shape=(2, 3))
loss = losses.log_loss(self._labels, tf_predictions, tf_weights)

with self.cached_session() as sess:
    loss = sess.run(loss, feed_dict={tf_predictions: self._np_predictions})
    self.assertAlmostEqual(-np.sum(expected_losses), loss, 3)
