# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    logits = constant_op.constant([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0],
                                   [0.0, 0.0, 10.0]])
    labels = constant_op.constant([0, 1, 2])
    loss = losses.sparse_softmax_cross_entropy(labels, logits)
    self.assertEqual(loss.op.name, 'sparse_softmax_cross_entropy_loss/value')
    self.assertAlmostEqual(self.evaluate(loss), 0.0, 3)
