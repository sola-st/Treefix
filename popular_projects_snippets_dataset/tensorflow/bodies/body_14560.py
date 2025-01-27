# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
# Return an ndarray from the model.
inputs = tf.keras.layers.Input(shape=(10,))
output_layer = tf.keras.layers.Lambda(np.square)(inputs)
model = tf.keras.Model([inputs], output_layer)

values = onp.arange(10, dtype=onp.float32)
values_as_array = np.asarray(values)

result = model(values)
self.assertIsInstance(result, np.ndarray)
self.assertAllClose(result, onp.square(values))

result = model(values_as_array)
self.assertIsInstance(result, np.ndarray)
self.assertAllClose(result, onp.square(values))
