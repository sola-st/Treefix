# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = array_ops.placeholder(dtypes.float32)
labels = array_ops.placeholder(dtypes.int32)
weights = 1.0
with self.cached_session() as sess:
    loss = losses.sparse_softmax_cross_entropy(labels, logits, weights)
    loss_val = sess.run(loss,
                        feed_dict={
                            logits: [[10.0, 0.0, 0.0],
                                     [0.0, 10.0, 0.0],
                                     [0.0, 0.0, 10.0]],
                            labels: [[2], [0], [1]],
                        })
    self.assertAlmostEqual((1.0 + 1.0 + 1.0) * 10.0 / 3.0, loss_val, 3)
