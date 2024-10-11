# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
stddev = np.sqrt(self._units).astype(np.float32)
initial_value = np.random.randn(input_shape[1], self._units).astype(
    np.float32) / stddev
# Note that TF NumPy can interoperate with tf.Variable.
self.w = tf.Variable(initial_value, trainable=True)
