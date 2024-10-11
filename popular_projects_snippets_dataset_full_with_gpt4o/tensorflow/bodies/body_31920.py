# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with ops.Graph().as_default():
    raw_losses = array_ops.reshape(self._raw_losses, shape=(3, 2, 4, 1))
    weights = np.ones(shape=(3, 2, 4, 2))
    expected_error_msg = 'weights can not be broadcast to values'
    self.assertEqual(0, len(util.get_losses()))

    # Static check.
    with self.assertRaisesRegex(ValueError, expected_error_msg):
        losses.compute_weighted_loss(raw_losses, weights=weights)

    # Dynamic check.
    weights_placeholder = array_ops.placeholder(dtypes.float32)
    weighted_loss = losses.compute_weighted_loss(
        raw_losses, weights=weights_placeholder)
    self.assertEqual(1, len(util.get_losses()))
    with self.cached_session():
        with self.assertRaisesRegex(errors_impl.OpError, expected_error_msg):
            weighted_loss.eval(feed_dict={weights_placeholder: weights})
