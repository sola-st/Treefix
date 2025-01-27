# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
weights = np.array([3, 6, 5, 0, 4, 2]).reshape((2, 3))
expected_losses = np.multiply(self._expected_losses, weights)

tf_predictions = array_ops.placeholder(dtypes.float32, shape=[2, 3])
loss = losses.log_loss(
    self._labels,
    tf_predictions,
    constant_op.constant(
        weights, shape=(2, 3)))

with self.cached_session() as sess:
    loss = sess.run(loss, feed_dict={tf_predictions: self._np_predictions})
    self.assertAlmostEqual(-np.sum(expected_losses) / 5.0, loss, 3)
