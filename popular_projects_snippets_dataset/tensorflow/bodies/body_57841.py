# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test the model quantized by the new converter with numeric verify ops."""
root, func, calibration_gen = self._getIntegerQuantizeModel()

quantized_converter = lite.TFLiteConverterV2.from_concrete_functions([func],
                                                                     root)
quantized_converter.target_spec.supported_ops = [
    lite.OpsSet.TFLITE_BUILTINS_INT8
]
quantized_converter.representative_dataset = calibration_gen

# Create a TFLite model with new quantizer.
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.experimental_new_quantizer = True
production_tflite = quantized_converter.convert()
# Create a TFLite model with new quantizer and numeric verify ops.
quantized_converter._experimental_calibrate_only = True
calibrated = quantized_converter.convert()
debug_mode_tflite = mlir_quantize(
    calibrated,
    enable_numeric_verify=True,
    enable_whole_model_verify=whole_model_verify)

# Check if adding debug mode should output a different flatbuffer.
self.assertNotEqual(production_tflite, debug_mode_tflite)

# Check if newly added ops are numeric verify ops.
input_data = tf.constant(
    np.random.uniform(-1, 1, size=(1, 5, 5, 3)).astype(np.float32))

def examine_tflite_model(tflite_content, input_data):
    interpreter = Interpreter(
        model_content=tflite_content,
        experimental_op_resolver_type=OpResolverType
        .BUILTIN_WITHOUT_DEFAULT_DELEGATES)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    interpreter.set_tensor(input_details[0]['index'], input_data.numpy())
    interpreter.invoke()
    tensor_details = interpreter.get_tensor_details()
    exit(({
        details['name']: interpreter.get_tensor(details['index'])
        for details in interpreter.get_tensor_details()
    }, tensor_details))

tflite_result, _ = examine_tflite_model(production_tflite, input_data)
debug_mode_tflite_result, debug_tensor_details = examine_tflite_model(
    debug_mode_tflite, input_data)

# MLIR-based quantizer should output flatbuffer model with `tfl.quantize`.
num_production_quantize_ops = len([
    None for output_tensor_name in tflite_result
    if 'tfl.quantize' in output_tensor_name
])
self.assertEqual(num_production_quantize_ops, 1)
# MLIR-based quantizer should output flatbuffer model with `tfl.quantize`.
num_debug_quantize_ops = len([
    None for output_tensor_name in debug_mode_tflite_result
    if 'tfl.quantize' in output_tensor_name
])
# Two numbers should be equal.
self.assertEqual(num_production_quantize_ops, num_debug_quantize_ops)
# DebugMode TFLite flatbuffer should have NumericVerifyOps more than zero.
# The name has the prefix "NumericVerify/{name}:{id}
# where {name} is the tensor name of the original quantized op's activation,
# and {id} is its tensor id.
num_debug_ops = 0
for output_tensor_name in debug_mode_tflite_result:
    if 'NumericVerify' in output_tensor_name:
        pos_end_prefix = len('NumericVerify/')
        pos_colon = output_tensor_name.rfind(':')
        self.assertEqual('NumericVerify/', output_tensor_name[:pos_end_prefix])
        tensor_id = int(output_tensor_name[pos_colon + 1:])
        original_tensor_name = output_tensor_name[pos_end_prefix:pos_colon]
        self.assertEqual(original_tensor_name,
                         debug_tensor_details[tensor_id]['name'])
        num_debug_ops += 1
self.assertEqual(num_debug_ops, 1)
# The number of debug ops should be equal to that of quantized ops.
self.assertEqual(num_debug_ops, num_debug_quantize_ops)
