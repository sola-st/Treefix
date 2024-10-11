# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = constant_op.constant([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0],
                               [0.0, 0.0, 10.0]])
labels = constant_op.constant([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
with self.cached_session():
    with self.assertRaises(ValueError):
        losses.softmax_cross_entropy(labels, logits, weights=None)
