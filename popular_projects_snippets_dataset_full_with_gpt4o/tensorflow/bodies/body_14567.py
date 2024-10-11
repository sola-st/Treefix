# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
with tf.GradientTape() as g:
    x = np.asarray([1., 2.])
    y = np.asarray([3., 4.])
    g.watch(x)
    g.watch(y)
    z = x * x * y

jacobian = g.jacobian(z, [x, y])
answer = [tf.linalg.diag(2 * x * y), tf.linalg.diag(x * x)]

self.assertIsInstance(jacobian[0], np.ndarray)
self.assertIsInstance(jacobian[1], np.ndarray)
self.assertAllClose(jacobian, answer)
