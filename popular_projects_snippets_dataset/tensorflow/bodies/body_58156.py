# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(4,), dtype=tf.uint32),
    tf.keras.layers.Reshape(target_shape=(2, 2))
])
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()[0]
output_details = interpreter.get_output_details()[0]

self.assertEqual(input_details["dtype"], np.uint32)
self.assertEqual(output_details["dtype"], np.uint32)

in_array = np.array([[1, 1, 1, 1]], dtype="uint32") * ((1 << 32) - 1)
expected_out = np.reshape(in_array, (2, 2))

interpreter.set_tensor(input_details["index"], in_array)
interpreter.invoke()

output_data = interpreter.get_tensor(output_details["index"])[0]
self.assertAllEqual(expected_out, output_data)
