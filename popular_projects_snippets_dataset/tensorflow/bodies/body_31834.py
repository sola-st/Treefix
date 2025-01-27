# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
"""The label tensor has incorrect number of elements."""
with self.cached_session():
    logits = constant_op.constant([[100.0, -100.0, -100.0],
                                   [-100.0, 100.0, -100.0],
                                   [-100.0, -100.0, 100.0]])
    labels = constant_op.constant([[0], [1], [2], [3]])
    weights = constant_op.constant([1.2, 3.4, 5.6])

    with self.assertRaises(ValueError):
        losses.sparse_softmax_cross_entropy(
            labels, logits, weights=weights).eval()
