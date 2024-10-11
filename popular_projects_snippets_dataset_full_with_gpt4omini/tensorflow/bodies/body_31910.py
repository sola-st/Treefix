# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
tf_predictions = array_ops.placeholder(
    dtypes.float32, shape=self._labels.shape)
loss = losses.cosine_distance(
    predictions=tf_predictions,
    labels=constant_op.constant(self._labels),
    dim=2,
    weights=constant_op.constant(
        [1, 0, 0, 1, 1, 1], shape=(3, 2, 1)))
with self.cached_session() as sess:
    loss = sess.run(loss, feed_dict={tf_predictions: self._predictions})
    self.assertEqual(3.0 / 4.0, loss)
