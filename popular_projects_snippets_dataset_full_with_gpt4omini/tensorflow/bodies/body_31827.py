# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = array_ops.placeholder(dtypes.float32, shape=(None, 3))
labels = array_ops.placeholder(dtypes.int32, shape=(None, 1))
weights = array_ops.placeholder(dtypes.float32)
with self.cached_session() as sess:
    loss = losses.sparse_softmax_cross_entropy(labels, logits, weights)
    loss_val = sess.run(loss,
                        feed_dict={
                            logits: [[10.0, 0.0, 0.0],
                                     [0.0, 10.0, 0.0],
                                     [0.0, 0.0, 10.0]],
                            labels: [[2], [0], [1]],
                            weights: ((1.2,), (3.4,), (5.6,)),
                        })
    self.assertAlmostEqual((1.2 + 3.4 + 5.6) * 10.0 / 3.0, loss_val, 3)
