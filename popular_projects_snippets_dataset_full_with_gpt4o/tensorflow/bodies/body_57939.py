# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
input_data = tf.constant(
    np.array(np.random.random_sample((4, 10, 10)), dtype=np.float32))
# Specify a fixed batch size(4) for the test model.
x = tf.keras.layers.Input(batch_shape=(4, 10, 10))
y = rnn_layer(units=10, input_shape=(10, 10))(x)
model = tf.keras.Model(inputs=[x], outputs=[y])

# Convert model.
converter = lite.TFLiteConverterV2.from_keras_model(model)
tflite_model = converter.convert()
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])[0]

# Check values from converted model.
expected_value = model.predict(input_data)
self.assertAllClose(expected_value, actual_value, atol=1e-05)
