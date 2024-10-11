# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
"""The label tensor has incorrect shape."""
with self.cached_session():
    logits = constant_op.constant([[100.0, -100.0, -100.0, -100.0],
                                   [-100.0, 100.0, -100.0, -100.0],
                                   [-100.0, -100.0, 100.0, -100.0],
                                   [-100.0, -100.0, -100.0, 100.0]])
    labels = constant_op.constant([[0, 1], [2, 3]])
    weights = constant_op.constant(1.2)

    with self.assertRaisesRegex(
        ValueError,
        '`labels.shape.rank` must equal `logits.shape.rank - 1`'):
        losses.sparse_softmax_cross_entropy(
            labels, logits, weights=weights).eval()
