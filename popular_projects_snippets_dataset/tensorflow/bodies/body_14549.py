# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
arr = np.asarray(0.)
t = tf.constant(10.)

arr_plus_t = arr + t
t_plus_arr = t + arr

self.assertIsInstance(arr_plus_t, tf.Tensor)
self.assertIsInstance(t_plus_arr, tf.Tensor)
self.assertEqual(10., arr_plus_t.numpy())
self.assertEqual(10., t_plus_arr.numpy())
