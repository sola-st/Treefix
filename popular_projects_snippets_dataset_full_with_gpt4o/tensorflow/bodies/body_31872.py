# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    predictions = constant_op.constant([[1.5, -1.4, -1.0, 0.0],
                                        [1.5, -1.4, -1.0, 0.0]])
    labels = constant_op.constant([[1.0, -1.0, 0.0, 0.5],
                                   [0.0, 1.0, 0.0, 1.5]])
    loss = losses.huber_loss(labels, predictions)
    quadratic = 0.5 * (0.25 + 0.16 + 1.0 + 0.25) / 4.
    linear = (1.5 + 2.4 + 1.0 + 1.5) / 4. - 0.5
    expected_loss = (quadratic + linear) / 2.
    self.assertAllClose(loss, expected_loss, atol=1e-5)
