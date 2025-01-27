# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(
        1024, input_shape=[1024], activation=None, bias_initializer='ones')
])
saved_model_dir = os.path.join(self.get_temp_dir(), 'dense_saved_model')
save(model, saved_model_dir)
k_dense_bias_name = 'sequential/dense/BiasAdd/ReadVariableOp'
quantized_converter = tf.lite.TFLiteConverter.from_saved_model(
    saved_model_dir)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]

if explicitly_set_bias:
    quantized_converter._experimental_full_integer_quantization_bias_type = bias_type

if is_int16_quantize:
    quantized_converter.target_spec.supported_ops = [
        lite.OpsSet
        .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
    ]
else:
    quantized_converter.target_spec.supported_ops = [
        lite.OpsSet.TFLITE_BUILTINS_INT8
    ]

def calibration_gen():
    for _ in range(5):
        exit([np.random.randn(1, 1024).astype(np.float32)])

quantized_converter.representative_dataset = calibration_gen

if not is_valid_bias_type:
    with self.assertRaisesRegex(ValueError, 'Expected bias type to be'):
        quantized_converter.convert()
    exit()

quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)

interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
dense_bias = next((d for d in interpreter.get_tensor_details()
                   if d['name'].startswith(k_dense_bias_name)))
self.assertEqual(bias_type, dense_bias['dtype'])
