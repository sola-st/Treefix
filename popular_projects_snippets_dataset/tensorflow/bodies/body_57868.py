# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test converting SignatureDef is correct and uses SignatureDef API.

    This test uses None as signature_key to test default behavior.
    """
root = self._getMultiFunctionModel()
input_data_0 = tf.constant(1., shape=[1])
input_data_1 = tf.constant(3., shape=[1])
mul_add_func = root.mul_add.get_concrete_function(input_data_1,
                                                  input_data_0)

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save(root, save_dir, {'mul_add': mul_add_func})

converter = lite.TFLiteConverterV2.from_saved_model(
    save_dir, signature_keys=['mul_add'])
tflite_model = converter.convert()

# Check values from converted model.
expected_value = root.mul_add(input_data_1, input_data_0)
interpreter = Interpreter(model_content=tflite_model)
signature_defs = interpreter.get_signature_list()
results = self._evaluateTFLiteModelUsingSignatureDef(
    tflite_model, None, {
        'y': input_data_0,
        'x': input_data_1
    })
self.assertEqual(list(results.keys()), ['output_0'])
self.assertEqual(expected_value.numpy(), results['output_0'])

# Verify the SignatureDef structure returned is as expected.
self.assertEqual(len(signature_defs), 1)
self.assertEqual(list(signature_defs.keys()), ['mul_add'])
self.assertEqual(len(signature_defs.values()), 1)
self.assertEqual(
    list(signature_defs['mul_add'].keys()), ['inputs', 'outputs'])
self.assertCountEqual(signature_defs['mul_add']['inputs'], ['x', 'y'])
self.assertEqual(list(signature_defs['mul_add']['outputs']), ['output_0'])
