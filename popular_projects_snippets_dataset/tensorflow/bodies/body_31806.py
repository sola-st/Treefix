# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = constant_op.constant([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0],
                               [0.0, 0.0, 10.0]])
labels = constant_op.constant([[0, 0, 1], [1, 0, 0], [0, 1, 0]])

with self.cached_session():
    loss = losses.softmax_cross_entropy(labels, logits)
    self.assertEqual(loss.op.name, 'softmax_cross_entropy_loss/value')
    self.assertAlmostEqual(self.evaluate(loss), 10.0, 3)
