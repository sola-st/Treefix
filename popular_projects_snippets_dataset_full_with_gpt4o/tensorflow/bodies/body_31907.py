# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
predictions = np.matrix(
    ('0.819031913261206 0.567041924552012 0.087465312324590;'
     '-0.665139432070255 -0.739487441769973 -0.103671883216994;'
     '0.707106781186548 -0.707106781186548 0'))
labels = np.matrix(('0.819031913261206 0.567041924552012 0.087465312324590;'
                    '0.665139432070255 0.739487441769973 0.103671883216994;'
                    '0.707106781186548 0.707106781186548 0'))

tf_preds = constant_op.constant(
    predictions, shape=(3, 1, 3), dtype=dtypes.float32)
tf_labels = constant_op.constant(
    labels, shape=(3, 1, 3), dtype=dtypes.float32)
loss = losses.cosine_distance(tf_labels, tf_preds, dim=2)

with self.cached_session():
    self.assertAlmostEqual(1.0, self.evaluate(loss), 5)
