# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
with tf.GradientTape() as g:
    x = np.asarray([[1., 2.], [3., 4.]])
    y = np.asarray([[3., 4.], [5., 6.]])
    g.watch(x)
    g.watch(y)
    z = x * x * y

batch_jacobian = g.batch_jacobian(z, x)
answer = tf.stack(
    [tf.linalg.diag(2 * x[0] * y[0]),
     tf.linalg.diag(2 * x[1] * y[1])])

self.assertIsInstance(batch_jacobian, np.ndarray)
self.assertAllClose(batch_jacobian, answer)
