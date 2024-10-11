# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Create a simple FullyConnected Model with an output of three dimensions."""
input_tensor = tf.keras.layers.Input(
    batch_size=1, shape=[3, 3], name='input_tensor', dtype=tf.float32)

x = tf.quantization.fake_quant_with_min_max_args(input_tensor, -3.0, 3.0)
x = tf.keras.layers.Dense(3)(x)
x = tf.quantization.fake_quant_with_min_max_args(x, -3.0, 3.0)
model = tf.keras.Model(input_tensor, x)

model.compile(
    optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Export the keras model to saved model.
saved_model_dir = os.path.join(self.get_temp_dir(),
                               'fully_connected_output_3d')
model.save(saved_model_dir, save_format='tf', include_optimizer=False)
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [lite.Optimize.DEFAULT]
tflite_model = converter.convert()
self.assertTrue(tflite_model)

interpreter = Interpreter(model_content=tflite_model)
output_details = interpreter.get_output_details()
input_details = interpreter.get_input_details()
interpreter.allocate_tensors()

input_data = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

actual_value = interpreter.get_tensor(output_details[0]['index'])
expected_value = model.predict(input_data)

self.assertLen(output_details[0]['shape_signature'], 3)
self.assertAllClose(expected_value, actual_value, atol=1e-1)
self.assertEqual(
    list(output_details[0]['shape_signature']),
    list(model.layers[-1].output_shape))
