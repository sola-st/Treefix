# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    logits = constant_op.constant([[100.0, -100.0, -100.0],
                                   [-100.0, 100.0, -100.0],
                                   [-100.0, -100.0, 100.0]])
    labels = constant_op.constant([[0], [1], [2]])
    weights = constant_op.constant([[3, 4, 5], [2, 6, 0], [8, 0, 1]])

    with self.assertRaises(ValueError):
        losses.sparse_softmax_cross_entropy(
            labels, logits, weights=weights).eval()
