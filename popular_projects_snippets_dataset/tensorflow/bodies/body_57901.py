# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
num_filters = 1024
conv_name = 'sequential/conv2d/Conv2D'
model = tf.keras.models.Sequential(
    [tf.keras.Input(shape=(32, 32, 3)),
     tf.keras.layers.Conv2D(num_filters, (3, 3), activation='relu')])
model.build()

converter = lite.TFLiteConverterV2.from_keras_model(model)
converter.optimizations = [lite.Optimize.DEFAULT]
converter.experimental_new_dynamic_range_quantizer = (
    enable_new_dynamic_range_quantizer)
converter._experimental_disable_per_channel = disable_per_channel
if enable_float16_quant:
    converter.target_spec.supported_types = [tf.float16]
quantized_tflite_model = converter.convert()
self.assertIsNotNone(quantized_tflite_model)

interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
quantized_weight = None
quantized_weight_with_one_postfix = None
quantized_weight_without_one_postfix = None
for d in interpreter.get_tensor_details():
    if d['name'] == conv_name + '1':
        quantized_weight = d
        quantized_weight_with_one_postfix = d
        break
for d in interpreter.get_tensor_details():
    if d['name'].startswith(conv_name):
        if quantized_weight is None:
            quantized_weight = d
        quantized_weight_without_one_postfix = d
        break

self.assertIsNotNone(quantized_weight)
quant_params = quantized_weight['quantization_parameters']

if enable_float16_quant:
    expected_num_params = 0
else:
    expected_num_params = 1 if disable_per_channel else num_filters
self.assertLen(quant_params['scales'], expected_num_params)
self.assertLen(quant_params['zero_points'], expected_num_params)

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertEqual(np.float32, output_details[0]['dtype'])
if enable_float16_quant:
    self.assertTrue(
        (quantized_weight_with_one_postfix is not None and
         np.float16 == quantized_weight_with_one_postfix['dtype']) or
        (quantized_weight_without_one_postfix is not None and
         np.float16 == quantized_weight_without_one_postfix['dtype']))
else:
    self.assertEqual(np.int8, quantized_weight['dtype'])
