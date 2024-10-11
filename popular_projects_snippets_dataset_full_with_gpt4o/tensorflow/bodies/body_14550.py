# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
t = tf.constant(10.)

sq = np.square(t)
self.assertIsInstance(sq, np.ndarray)
self.assertEqual(100., sq)
