# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
# Dynamic range quant requires total num elements of filters > 1024.
k_num_filters = 38
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(k_num_filters, (3, 3), activation='relu')
])
model.build(input_shape=(1, 5, 5, 3))
saved_model_dir = os.path.join(self.get_temp_dir(), 'conv_saved_model')
save(model, saved_model_dir)
k_conv_name = 'sequential/conv2d/Conv2D'
quantized_converter = tf.lite.TFLiteConverter.from_saved_model(
    saved_model_dir)
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
if representative_dataset:
    def calib_gen():
        for _ in range(5):
            exit([np.random.uniform(-1, 1, size=(1, 5, 5, 3)).astype(np.float32)])
    quantized_converter.representative_dataset = calib_gen
quantized_converter.target_spec.supported_ops = [
    lite.OpsSet.TFLITE_BUILTINS
]
quantized_converter.experimental_new_quantizer = enable_mlir_quantizer
if disable_per_channel:
    quantized_converter._experimental_disable_per_channel = (
        disable_per_channel)
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)

interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
detail = next((d for d in interpreter.get_tensor_details()
               if d['name'].startswith(k_conv_name)))
quant_params = detail['quantization_parameters']
expected_num_params = k_num_filters
if disable_per_channel:
    expected_num_params = 1
self.assertLen(quant_params['scales'], expected_num_params)
self.assertLen(quant_params['zero_points'], expected_num_params)
