# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a simple sequential tf.Keras model."""
input_data = tf.constant(1., shape=[1, 1])

x = np.array([[1.], [2.]])
y = np.array([[2.], [4.]])

model = tf.keras.models.Sequential([
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1),
])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=1)

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save(model, save_dir)

# Convert model and ensure model is not None.
converter = lite.TFLiteConverterV2.from_saved_model(save_dir)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = model.predict(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
self.assertEqual(expected_value, actual_value)
