# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    delta = 0.5
    predictions = constant_op.constant([1.5, -1.4, -0.5, 0.0])
    labels = constant_op.constant([1.0, -1.0, 0.0, 0.5])
    expected = 0.5 * np.array([0.5**2, 0.4**2, 0.5**2, 0.5**2]).mean()
    loss = losses.huber_loss(labels, predictions, delta=delta)
    self.assertAllClose(expected, self.evaluate(loss), atol=1e-5)
