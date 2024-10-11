# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
tf_var = tf.Variable(2.0)
value = np.square(tf_var)
self.assertIsInstance(value, np.ndarray)
self.assertAllClose(4.0, value)
with tf.control_dependencies([tf_var.assign_add(value)]):
    tf_var_value = tf_var.read_value()
self.assertAllClose(6.0, tf_var_value)
