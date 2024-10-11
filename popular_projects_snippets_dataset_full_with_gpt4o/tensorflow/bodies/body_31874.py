# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
delta = 0.5
predictions = constant_op.constant([1.5, -1.4, -1.0, 0.0])
labels = constant_op.constant([0.0, 1.0, 0.0, 1.5])
expected = delta * np.array([1.5, 2.4, 1.0, 1.5]).mean()
expected -= 0.5 * delta**2
loss = losses.huber_loss(labels, predictions, delta=delta)
with self.cached_session():
    self.assertAllClose(expected, self.evaluate(loss), atol=1e-5)
