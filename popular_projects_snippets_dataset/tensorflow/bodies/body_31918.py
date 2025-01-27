# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with ops.Graph().as_default():
    self.assertEqual(0, len(util.get_losses()))
    expected_error_msg = 'weights can not be broadcast to values'

    # Static check.
    with self.assertRaisesRegex(ValueError, expected_error_msg):
        losses.compute_weighted_loss(self._raw_losses, weights=weights)

    # Dynamic check.
    weights_placeholder = array_ops.placeholder(dtypes.float32)
    weighted_loss = losses.compute_weighted_loss(
        self._raw_losses, weights=weights_placeholder)
    self.assertEqual(1, len(util.get_losses()))
    with self.cached_session():
        with self.assertRaisesRegex(errors_impl.OpError, expected_error_msg):
            weighted_loss.eval(feed_dict={weights_placeholder: weights})
