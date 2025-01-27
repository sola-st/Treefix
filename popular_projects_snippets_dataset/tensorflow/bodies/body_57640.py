# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    inp, output, calibration_gen = self._getIntegerQuantizeModel()
    sess = session.Session()

bias_idx = 1
bias_name = 'Conv2D'

# Convert float model.
float_converter = lite.TFLiteConverter.from_session(sess, [inp], [output])
float_tflite_model = float_converter.convert()
self.assertIsNotNone(float_tflite_model)
interpreter = Interpreter(model_content=float_tflite_model)
interpreter.allocate_tensors()
self.assertEqual(interpreter.get_tensor_details()[bias_idx]['name'],
                 bias_name)
self.assertEqual(interpreter.get_tensor_details()[bias_idx]['dtype'],
                 dtypes.float32)

# Convert model to quantized version
quantized_converter = lite.TFLiteConverter.from_session(
    sess, [inp], [output])
quantized_converter.experimental_new_quantizer = enable_mlir_quantizer
quantized_converter.optimizations = [lite.Optimize.DEFAULT]
quantized_converter.target_spec.supported_types = [dtypes.float16]
if include_int8:
    quantized_converter.target_spec.supported_types.append(dtypes.int8)
if use_rep_data:
    quantized_converter.representative_dataset = calibration_gen
if is_float16_accumulation:
    quantized_converter.target_spec.experimental_supported_accumulation_type = dtypes.float16  # pylint: disable=line-too-long

else:
    quantized_tflite_model = quantized_converter.convert()
    self.assertIsNotNone(quantized_tflite_model)
    metadata = get_conversion_metadata(quantized_tflite_model)
    self.assertIsNotNone(metadata)
    self.assertAllEqual(expected_opt_modes,
                        metadata.options.modelOptimizationModes)
    interpreter = Interpreter(model_content=quantized_tflite_model)
    interpreter.allocate_tensors()

    # MLIR quantizer has different bias index.
    bias_tensor = [
        tensor for tensor in interpreter.get_tensor_details()
        if tensor['name'] == bias_name
    ]
    self.assertLen(bias_tensor, 1)

    if is_float16_quantized:
        # Verify that bias constant is float16 type.
        self.assertEqual(bias_tensor[0]['dtype'], dtypes.float16)
    elif is_post_training_quantized:
        # Verify that bias constants is int32 type.
        self.assertEqual(bias_tensor[0]['dtype'], dtypes.int32)
    else:
        raise ValueError('Invalid test options.')
