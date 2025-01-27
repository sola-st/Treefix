# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        shape=[5, 5], dtype=dtypes.float32, name='input')
    out_tensor = in_tensor + in_tensor
    logging_ops.print_v2(out_tensor)
    sess = session.Session()

converter = lite.TFLiteConverter(
    sess.graph_def,
    input_tensors=None,
    output_tensors=None,
    input_arrays_with_shape=[('input', [5, 5])],
    output_arrays=None,
    experimental_debug_info_func=None)
converter._control_output_arrays = ['PrintV2']
converter.target_spec.supported_ops = [
    lite.OpsSet.TFLITE_BUILTINS,
    lite.OpsSet.SELECT_TF_OPS,
]
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

model = util._convert_model_from_bytearray_to_object(tflite_model)
self.assertEqual(model.operatorCodes[0].builtinCode,
                 schema_fb.BuiltinOperator.ADD)
self.assertEqual(model.operatorCodes[1].builtinCode,
                 schema_fb.BuiltinOperator.CUSTOM)
self.assertEqual(model.operatorCodes[1].customCode, b'FlexStringFormat')
self.assertEqual(model.operatorCodes[2].builtinCode,
                 schema_fb.BuiltinOperator.CUSTOM)
self.assertEqual(model.operatorCodes[2].customCode, b'FlexPrintV2')

# Check values from converted model.
interpreter = Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
self.assertLen(input_details, 1)
self.assertEqual('input', input_details[0]['name'])
self.assertEqual(np.float32, input_details[0]['dtype'])
self.assertAllEqual([5, 5], input_details[0]['shape'])
self.assertEqual((0., 0.), input_details[0]['quantization'])

output_details = interpreter.get_output_details()
self.assertLen(output_details, 0)
