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
add_signature_runner = interpreter.get_signature_runner('add')
add_output = add_signature_runner(x=input_data)
self.assertEqual(add_output['output_0'], 3)

sub_signature_runner = interpreter.get_signature_runner('sub')
sub_output = sub_signature_runner(x=input_data)
self.assertEqual(sub_output['output_0'], -2)
