# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
with tf.GradientTape() as t:
    x = np.asarray(3.0)
    y = np.asarray(2.0)

    t.watch([x, y])

    xx = 2 * x
    yy = 3 * y

dx, dy = t.gradient([xx, yy], [x, y])

self.assertIsInstance(dx, np.ndarray)
self.assertIsInstance(dy, np.ndarray)
self.assertAllClose(dx, 2.0)
self.assertAllClose(dy, 3.0)
