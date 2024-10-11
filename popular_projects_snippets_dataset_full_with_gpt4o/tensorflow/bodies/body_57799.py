# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Convert multiple functions in a multi-functional model."""
root = self._getMultiFunctionModel()
input_data = tf.constant(1., shape=[1])
add_func = root.add.get_concrete_function(input_data)
sub_func = root.sub.get_concrete_function(input_data)

# Try converting multiple functions.
converter = lite.TFLiteConverterV2.from_concrete_functions(
    [add_func, sub_func], root)
tflite_model = converter.convert()

# Check signatures are valid from converted model.
interpreter = Interpreter(model_content=tflite_model)
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
add_signature_runner = interpreter.get_signature_runner('add')
add_output = add_signature_runner(x=input_data)
self.assertEqual(add_output['output_0'], 3)
input_details = add_signature_runner.get_input_details()
self.assertEqual(1, len(input_details))
self.assertEqual('add_x:0', input_details['x']['name'])
self.assertEqual(np.float32, input_details['x']['dtype'])
self.assertTrue(([1] == input_details['x']['shape']).all())
self.assertEqual((0.0, 0), input_details['x']['quantization'])

sub_signature_runner = interpreter.get_signature_runner('sub')
sub_output = sub_signature_runner(x=input_data)
self.assertEqual(sub_output['output_0'], -2)
output_details = sub_signature_runner.get_output_details()
self.assertEqual(1, len(output_details))
self.assertEqual('StatefulPartitionedCall_1:0',
                 output_details['output_0']['name'])
self.assertEqual(np.float32, output_details['output_0']['dtype'])
self.assertTrue(([1] == output_details['output_0']['shape']).all())
self.assertEqual((0.0, 0), output_details['output_0']['quantization'])

# Check the conversion metadata.
metadata = get_conversion_metadata(tflite_model)
self.assertIsNotNone(metadata)
self.assertEqual(metadata.environment.apiVersion, 2)
self.assertEqual(metadata.environment.modelType,
                 metadata_fb.ModelType.TF_CONCRETE_FUNCTIONS)
self.assertAllEqual([], metadata.options.modelOptimizationModes)
