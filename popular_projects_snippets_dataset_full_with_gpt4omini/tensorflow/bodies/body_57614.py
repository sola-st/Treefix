# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor_a = array_ops.placeholder(shape=[3], dtype=dtypes.float32)
    in_tensor_b = array_ops.placeholder(shape=[3], dtype=dtypes.float32)
    # ceil kernel does not support int8 nor int16 types neither.
    left = math_ops.ceil(in_tensor_a)
    out_tensor_b = math_ops.tanh(in_tensor_b)
    add = math_ops.add(left, out_tensor_b)
    # ceil kernel does not support int8 nor int16 types neither.
    out_tensor_a = math_ops.ceil(add)
    sess = session.Session()

def calibration_gen():
    for _ in range(5):
        exit([
            np.random.uniform(-1, 1, size=(3)).astype(np.float32),
            np.random.uniform(-1, 1, size=(3)).astype(np.float32)
        ])

quantized_converter = lite.TFLiteConverter.from_session(
    sess, [in_tensor_a, in_tensor_b], [out_tensor_a, out_tensor_b])
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.representative_dataset = calibration_gen
if is_int_only:
    if is_int16_quantize:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet
            .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8,
            lite.OpsSet.TFLITE_BUILTINS
        ]
    else:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.TFLITE_BUILTINS_INT8, lite.OpsSet.TFLITE_BUILTINS
        ]
else:
    if is_int16_quantize:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet
            .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8,
            lite.OpsSet.TFLITE_BUILTINS
        ]
    else:
        quantized_converter.target_spec.supported_ops = [
            lite.OpsSet.TFLITE_BUILTINS
        ]

quantized_converter.inference_input_type = inference_input_output_type
quantized_converter.inference_output_type = inference_input_output_type
quantized_converter.experimental_new_quantizer = enable_mlir_quantizer
quantized_tflite_model = quantized_converter.convert()
self.assertIsNotNone(quantized_tflite_model)

expected_dtype = inference_input_output_type.as_numpy_dtype
# Allow float32 for fallback on non-quantizable op.
expected_ceil_dtype = (
    expected_dtype if enable_mlir_quantizer else dtypes.float32)

interpreter = Interpreter(model_content=quantized_tflite_model)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
self.assertLen(input_details, 2)
self.assertEqual(input_details[0]['dtype'], expected_ceil_dtype)
self.assertEqual(input_details[1]['dtype'], expected_dtype)
output_details = interpreter.get_output_details()
self.assertLen(output_details, 2)
self.assertEqual(output_details[0]['dtype'], expected_ceil_dtype)
self.assertEqual(output_details[1]['dtype'], expected_dtype)
