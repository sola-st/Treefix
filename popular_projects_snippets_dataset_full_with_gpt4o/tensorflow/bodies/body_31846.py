# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    label_smoothing = 0.1
    sigmoid_logits = constant_op.constant([[100.0, -100.0, -100.0]])
    sigmoid_labels = constant_op.constant([[1, 0, 1]])
    sigmoid_loss = losses.sigmoid_cross_entropy(
        sigmoid_labels, sigmoid_logits, label_smoothing=label_smoothing)
    self.assertEqual(sigmoid_logits.dtype, sigmoid_loss.dtype)

    softmax_logits = constant_op.constant(
        [[0.0, 100.0], [100.0, 0.0], [100.0, 0.0]])
    softmax_labels = constant_op.constant([[0, 1], [1, 0], [0, 1]])
    softmax_loss = losses.softmax_cross_entropy(
        softmax_labels, softmax_logits, label_smoothing=label_smoothing)
    self.assertAlmostEqual(
        self.evaluate(sigmoid_loss), self.evaluate(softmax_loss), 3)
