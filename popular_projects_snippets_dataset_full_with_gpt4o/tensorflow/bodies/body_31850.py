# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
tf_predictions = array_ops.placeholder(
    dtypes.float32, shape=self._np_labels.shape)
loss = losses.log_loss(self._labels, tf_predictions)
with self.cached_session():
    self.assertAlmostEqual(
        0.0, loss.eval(feed_dict={tf_predictions: self._np_labels}), 3)
