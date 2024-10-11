# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    x = array_ops.placeholder(dtypes.float32)
    y = array_ops.identity(x)
    dy = indexed_slices.IndexedSlices(
        array_ops.placeholder(dtypes.float32),
        array_ops.placeholder(dtypes.int32))
    dx, = gradients.gradients(y, x, grad_ys=dy)
    # The IndexedSlices gradient of tf.identity is the identity map.
    with self.cached_session() as sess:
        vdx, vdy = sess.run(
            [dx, dy], feed_dict={x: [1.0], dy.indices: [0], dy.values: [2.0]})
    self.assertEqual(vdx, vdy)
