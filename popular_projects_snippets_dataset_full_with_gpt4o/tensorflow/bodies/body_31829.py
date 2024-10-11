# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = constant_op.constant([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0],
                               [0.0, 0.0, 10.0]])
labels = constant_op.constant([[2], [0], [1]])
weights = constant_op.constant([[1.2], [3.4], [5.6]])
with self.cached_session():
    loss = losses.sparse_softmax_cross_entropy(labels, logits, weights)
    self.assertAlmostEqual((1.2 + 3.4 + 5.6) * 10.0 / 3.0,
                           self.evaluate(loss), 3)
