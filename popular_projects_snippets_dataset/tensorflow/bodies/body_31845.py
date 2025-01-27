# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    logits = constant_op.constant([[100.0, -100.0, -100.0]])
    labels = constant_op.constant([[1, 0, 1]])
    # Sigmoid cross entropy loss is:
    #   max(x,0) - x*z + log(1 + exp(-abs(x)))
    # The new labels are:
    #    z' = z * (1 - L) + 0.5 L
    #    1 -> 1 - 0.5 L
    #    0 -> 0.5 L
    # here we expect:
    # 1/3 * (100 - 100 * (1 - 0.5 L)  + 0
    #       + 0  + 100 * (0.5 L)      + 0
    #       + 0  + 100 * (1 - 0.5 L)  + 0)
    # = 1/3 * (100 + 50 L)
    label_smoothing = 0.1
    loss = losses.sigmoid_cross_entropy(
        labels, logits, label_smoothing=label_smoothing)
    self.assertEqual(logits.dtype, loss.dtype)
    self.assertEqual('sigmoid_cross_entropy_loss/value', loss.op.name)
    expected_value = (100.0 + 50.0 * label_smoothing) / 3.0
    self.assertAlmostEqual(self.evaluate(loss), expected_value, 3)
