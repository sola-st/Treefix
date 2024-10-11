# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
weight_values = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 5, 0, 0, 0, 3, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 7, 0, 0, 0, -6, -2, 0, 0, 0, 0, 0, -2, 0, 6],
])

custom_init = tf.constant_initializer(weight_values.transpose())
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(
        8, kernel_initializer=custom_init, input_shape=[16])
])

def calibration_gen():
    for _ in range(10):
        exit([np.random.uniform(-1, 1, size=(1, 16)).astype(np.float32) * 16])

quantized_converter = lite.TFLiteConverterV2.from_keras_model(model)
quantized_converter.optimizations = [
    lite.Optimize.EXPERIMENTAL_SPARSITY, lite.Optimize.DEFAULT
]
quantized_converter.representative_dataset = calibration_gen
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)

# Check the conversion metadata.
metadata = get_conversion_metadata(quantized_tflite_model)
self.assertIsNotNone(metadata)
self.assertEqual(
    metadata.environment.tensorflowVersion.decode('utf-8'),
    versions.__version__)
self.assertEqual(metadata.environment.apiVersion, 2)
self.assertAllEqual([
    metadata_fb.ModelOptimizationMode.PTQ_FULL_INTEGER,
    metadata_fb.ModelOptimizationMode.BLOCK_SPARSITY,
], metadata.options.modelOptimizationModes)

# Check values from converted model.
interpreter = Interpreter(model_content=quantized_tflite_model)
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
interpreter.allocate_tensors()
input_data = np.array(
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]],
    dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
actual_value = interpreter.get_tensor(output_details[0]['index'])
self.assertArrayNear(
    np.array([0, 87, 0, 0, 0, 0, 0, 34], dtype=np.float32),
    actual_value.flatten(),
    err=1)
