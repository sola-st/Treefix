# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = array_ops.placeholder(dtypes.float32, shape=(None, 1))
labels = array_ops.placeholder(dtypes.float32, shape=(None, 1))
weights = array_ops.ones_like(logits, dtype=dtypes.float32)

loss = losses.sigmoid_cross_entropy(labels, logits, weights)
self.assertEqual(logits.dtype, loss.dtype)

with self.cached_session() as sess:
    loss = sess.run(loss,
                    feed_dict={
                        logits: np.ones((32, 1)),
                        labels: np.ones((32, 1)),
                    })
    self.assertAlmostEqual(0.313, loss, 3)
