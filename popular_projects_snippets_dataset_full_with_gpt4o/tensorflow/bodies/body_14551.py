# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
arr = np.asarray(10.)

# TODO(nareshmodi): Test more ops.
sq = tf.square(arr)
self.assertIsInstance(sq, tf.Tensor)
self.assertEqual(100., sq.numpy())
