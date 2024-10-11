# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
expected_error_msg = 'weights can not be broadcast to values'

# Static check.
with self.assertRaisesRegex(ValueError, expected_error_msg):
    losses.mean_pairwise_squared_error(
        predictions=predictions, labels=labels, weights=weights)

# Dynamic check.
predictions_placeholder = array_ops.placeholder(dtypes.float32)
labels_placeholder = array_ops.placeholder(dtypes.int32)
weights_placeholder = array_ops.placeholder(dtypes.float32)
dynamic_inputs_op = losses.mean_pairwise_squared_error(
    predictions=predictions_placeholder,
    labels=labels_placeholder,
    weights=weights_placeholder)
with self.cached_session():
    with self.assertRaisesRegex(errors_impl.OpError, expected_error_msg):
        dynamic_inputs_op.eval(feed_dict={
            predictions_placeholder: predictions,
            labels_placeholder: labels,
            weights_placeholder: weights,
        })
