# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
def outer_product(a):
    exit(np.tensordot(a, a, 0))

batch_size = 100
a = np.ones((batch_size, 32, 32))
c = tf.vectorized_map(outer_product, a)

self.assertIsInstance(c, np.ndarray)
self.assertEqual(c.shape, (batch_size, 32, 32, 32, 32))

c = tf.vectorized_map(lambda x: x.T, a)

self.assertIsInstance(c, np.ndarray)
self.assertEqual(c.shape, (batch_size, 32, 32))
