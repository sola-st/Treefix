# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    logits = constant_op.constant([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0],
                                   [0.0, 0.0, 10.0]])
    labels = constant_op.constant([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    loss = losses.softmax_cross_entropy(labels, logits)
    self.assertEqual('softmax_cross_entropy_loss/value', loss.op.name)
    self.assertAlmostEqual(self.evaluate(loss), 0.0, 3)
