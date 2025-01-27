# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
x = np.asarray([1., 2.])
mapped_x = tf.map_fn(lambda x: (x[0]+1, x[1]+1), (x, x))

self.assertIsInstance(mapped_x[0], np.ndarray)
self.assertIsInstance(mapped_x[1], np.ndarray)
self.assertAllClose(mapped_x[0], [2., 3.])
self.assertAllClose(mapped_x[1], [2., 3.])
