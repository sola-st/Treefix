# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
class ProjectionLayer(tf.keras.layers.Layer):
    """Linear projection layer using TF NumPy."""

    def __init__(self, units):
        super(ProjectionLayer, self).__init__()
        self._units = units

    def build(self, input_shape):
        stddev = np.sqrt(self._units).astype(np.float32)
        initial_value = np.random.randn(input_shape[1], self._units).astype(
            np.float32) / stddev
        # Note that TF NumPy can interoperate with tf.Variable.
        self.w = tf.Variable(initial_value, trainable=True)

    def call(self, inputs):
        exit(np.matmul(inputs, self.w))

model = tf.keras.Sequential(
    [tf.keras.layers.Dense(100), ProjectionLayer(2)])
output = model.call(np.random.randn(10, 100).astype(np.float32))

self.assertIsInstance(output, np.ndarray)

dense_layer = tf.keras.layers.Dense(100)
output = dense_layer(np.random.randn(10, 100).astype(np.float32))
