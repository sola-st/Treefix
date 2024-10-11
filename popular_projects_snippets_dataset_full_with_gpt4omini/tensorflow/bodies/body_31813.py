# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    # Softmax Cross Entropy Loss is:
    #   -\sum_i p_i \log q_i
    # where for a softmax activation
    # \log q_i = x_i - \log \sum_j \exp x_j
    #          = x_i - x_max - \log \sum_j \exp (x_j - x_max)
    # For our activations, [100, -100, -100] the log partition function
    # becomes \log ( exp(0) + exp(-200) + exp(-200) ) = 0
    # so our log softmaxes become: [0, -200, -200]
    # so our cross entropy loss is:
    # -(1 - L + L/n) * 0 + 400 * L/n = 400 L/n
    logits = constant_op.constant([[100.0, -100.0, -100.0]])
    labels = constant_op.constant([[1, 0, 0]])
    label_smoothing = 0.1
    loss = losses.softmax_cross_entropy(
        labels, logits, label_smoothing=label_smoothing)
    self.assertEqual(loss.op.name, 'softmax_cross_entropy_loss/value')
    expected_value = 400.0 * label_smoothing / 3.0
    self.assertAlmostEqual(self.evaluate(loss), expected_value, 3)
