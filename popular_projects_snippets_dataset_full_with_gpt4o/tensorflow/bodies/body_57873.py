# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Convert multiple functions in a multi-functional model."""
root = self._getMultiFunctionModel()
input_data = tf.constant(1., shape=[1])
add_func = root.add.get_concrete_function(input_data)
sub_func = root.sub.get_concrete_function(input_data)

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save(root, save_dir, {'add': add_func, 'sub': sub_func})

# Try converting multiple functions.
converter = lite.TFLiteConverterV2.from_saved_model(save_dir)

def representative_dataset_gen():
    for _ in range(2):
        exit(('add', {
            'x': np.random.uniform(low=0, high=1, size=(1,)).astype(np.float32),
        }))
    for _ in range(2):
        exit(('sub', {
            'x': np.random.uniform(low=0, high=1, size=(1,)).astype(np.float32),
        }))

converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset_gen
if is_int_only:
    if is_int16_quantize:
        converter.target_spec.supported_ops = [
            lite.OpsSet
            .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
        ]
    else:
        converter.target_spec.supported_ops = [lite.OpsSet.TFLITE_BUILTINS_INT8]
else:
    if is_int16_quantize:
        converter.target_spec.supported_ops = [
            lite.OpsSet
            .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
        ]
    else:
        converter.target_spec.supported_ops = [lite.OpsSet.TFLITE_BUILTINS]
converter.inference_input_type = inference_input_output_type
converter.inference_output_type = inference_input_output_type
converter.experimental_new_quantizer = enable_mlir_quantizer
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

interpreter = tf.lite.Interpreter(model_content=tflite_model)
signature_defs = interpreter.get_signature_list()

# Verify the SignatureDef structure returned is as expected.
self.assertEqual(len(signature_defs), 2)
self.assertEqual(list(signature_defs.keys()), ['add', 'sub'])
self.assertEqual(len(signature_defs.values()), 2)
self.assertEqual(list(signature_defs['add'].keys()), ['inputs', 'outputs'])
self.assertCountEqual(signature_defs['add']['inputs'], ['x'])
self.assertEqual(list(signature_defs['add']['outputs']), ['output_0'])
self.assertEqual(list(signature_defs['sub'].keys()), ['inputs', 'outputs'])
self.assertCountEqual(signature_defs['sub']['inputs'], ['x'])
self.assertEqual(list(signature_defs['sub']['outputs']), ['output_0'])

# Verify the Signature runner executions.
input_data = tf.constant(
    np.random.uniform(-1, 1, size=(1,)).astype(
        inference_input_output_type.as_numpy_dtype))
add_signature_runner = interpreter.get_signature_runner('add')
add_output = add_signature_runner(x=input_data)
self.assertIsNotNone(add_output['output_0'])
input_details = add_signature_runner.get_input_details()
self.assertLen(input_details, 1)
self.assertStartsWith(input_details['x']['name'], 'add_x:0')
self.assertEqual(inference_input_output_type.as_numpy_dtype,
                 input_details['x']['dtype'])
self.assertTrue(([1] == input_details['x']['shape']).all())
if inference_input_output_type == dtypes.float32:
    self.assertEqual((0.0, 0), input_details['x']['quantization'])

sub_signature_runner = interpreter.get_signature_runner('sub')
sub_output = sub_signature_runner(x=input_data)
self.assertIsNotNone(sub_output['output_0'])
output_details = sub_signature_runner.get_output_details()
self.assertLen(output_details, 1)
self.assertStartsWith(output_details['output_0']['name'],
                      'StatefulPartitionedCall_1:0')
self.assertEqual(inference_input_output_type.as_numpy_dtype,
                 output_details['output_0']['dtype'])
self.assertTrue(([1] == output_details['output_0']['shape']).all())
if inference_input_output_type == dtypes.float32:
    self.assertEqual((0.0, 0), output_details['output_0']['quantization'])
