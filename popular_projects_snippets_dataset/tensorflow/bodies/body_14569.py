# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
x = np.asarray([1., 2.])
xt = np.asarray([3., 4.])
with tf.autodiff.ForwardAccumulator(x, xt) as acc:
    y = x * 2.
yt = acc.jvp(y)
self.assertIsInstance(yt, np.ndarray)
self.assertAllClose([6., 8.], yt)
z = np.asarray([1.])
self.assertIsNone(acc.jvp(z))
