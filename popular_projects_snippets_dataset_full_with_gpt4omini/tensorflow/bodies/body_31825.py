# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = constant_op.constant([[10.0, 0.0, 0.0],
                               [0.0, 10.0, 0.0],
                               [0.0, 0.0, 10.0]])
labels = constant_op.constant([[2], [0], [1]])
weights = array_ops.placeholder(dtypes.float32)
with self.cached_session() as sess:
    loss = losses.sparse_softmax_cross_entropy(labels, logits, weights)
    loss_val = sess.run(loss,
                        feed_dict={weights: ((1.2,), (3.4,), (5.6,))})
    self.assertAlmostEqual((1.2 + 3.4 + 5.6) * 10.0 / 3.0, loss_val, 3)
