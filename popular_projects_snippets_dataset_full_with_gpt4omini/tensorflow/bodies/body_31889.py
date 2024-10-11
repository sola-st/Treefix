# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    static_inputs_op = losses.mean_pairwise_squared_error(
        predictions=predictions, labels=labels, weights=weights)
    self.assertAlmostEqual(
        expected_loss, self.evaluate(static_inputs_op), places=3)

    predictions_placeholder = array_ops.placeholder(
        dtypes.float32, shape=np.asarray(predictions.shape))
    labels_placeholder = array_ops.placeholder(
        dtypes.int32, shape=np.asarray(labels.shape))
    weights_placeholder = array_ops.placeholder(
        dtypes.float32, shape=np.asarray(weights).shape)
    dynamic_inputs_op = losses.mean_pairwise_squared_error(
        predictions=predictions_placeholder,
        labels=labels_placeholder,
        weights=weights_placeholder)
    feed_dict = {
        predictions_placeholder: predictions,
        labels_placeholder: labels,
        weights_placeholder: weights,
    }
    self.assertAlmostEqual(
        expected_loss, dynamic_inputs_op.eval(feed_dict=feed_dict), places=3)
