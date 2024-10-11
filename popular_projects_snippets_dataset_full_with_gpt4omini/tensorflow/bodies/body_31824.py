# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = constant_op.constant([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0],
                               [0.0, 0.0, 10.0]])
labels = constant_op.constant([[2], [0], [1]])
weights = 2.3
with self.cached_session():
    loss = losses.sparse_softmax_cross_entropy(
        labels, logits, constant_op.constant((weights,)))
    self.assertAlmostEqual(weights * 10.0, self.evaluate(loss), 3)
