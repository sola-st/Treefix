# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a Functional tf.keras model with default inputs."""
with test_context():
    inputs = keras.layers.Input(shape=(3,), name='input')
    x = keras.layers.Dense(2)(inputs)
    output = keras.layers.Dense(3)(x)

    model = keras.models.Model(inputs, output)
    model.compile(
        loss=keras.losses.MSE,
        optimizer='sgd',
        metrics=[keras.metrics.categorical_accuracy])
    x = np.random.random((1, 3))
    y = np.random.random((1, 3))
    model.train_on_batch(x, y)

    model.predict(x)
    fd, self._keras_file = tempfile.mkstemp('.h5')
    try:
        keras.models.save_model(model, self._keras_file)
    finally:
        os.close(fd)

    # Convert to TFLite model.
    converter = lite.TFLiteConverter.from_keras_model_file(self._keras_file)
    tflite_model = converter.convert()
    self.assertIsNotNone(tflite_model)

# Check tensor details of converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('input', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([1, 3], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 1)
self.assertEqual(np.float32, output_details[0]['dtype'])
self.assertAllEqual([1, 3], output_details[0]['shape'])
self.assertEqual((0., 0.), output_details[0]['quantization'])

# Check inference of converted model.
input_data = np.array([[1, 2, 3]], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
tflite_result = interpreter.get_tensor(output_details[0]['index'])

keras_model = keras.models.load_model(self._keras_file)
keras_result = keras_model.predict(input_data)

np.testing.assert_almost_equal(tflite_result, keras_result, 5)
