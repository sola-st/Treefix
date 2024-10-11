# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
y = np.asarray(2.0)

with tf.GradientTape() as t:
    x = np.asarray(3.0)
    t.watch([x])
    z = 2 * x

dz = t.gradient(z, y)

self.assertIsNone(dz)
