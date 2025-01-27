# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    logits = constant_op.constant([[100.0, -100.0, -100.0],
                                   [-100.0, 100.0, -100.0],
                                   [-100.0, -100.0, 100.0]])
    labels = constant_op.constant([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    weights = constant_op.constant([[3, 4, 5], [2, 6, 0], [8, 0, 1]])
    loss = losses.sigmoid_cross_entropy(labels, logits, weights)
    self.assertEqual(logits.dtype, loss.dtype)
    self.assertEqual('sigmoid_cross_entropy_loss/value', loss.op.name)
    self.assertAlmostEqual(1700.0 / 7.0, self.evaluate(loss), 3)
