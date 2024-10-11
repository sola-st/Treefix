# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test converting SignatureDef is correct and uses SignatureDef API."""
root = self._getMultiFunctionModel()
input_data = tf.constant(1., shape=[1])
add_func = root.add.get_concrete_function(input_data)

converter = lite.TFLiteConverterV2([add_func], trackable_obj=root)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = add_func(input_data)
interpreter = Interpreter(model_content=tflite_model)
signature_defs = interpreter.get_signature_list()
results = self._evaluateTFLiteModelUsingSignatureDef(
    tflite_model, 'serving_default', {'x': input_data})
self.assertLen(list(results.keys()), 1)
self.assertStartsWith(list(results.keys())[0], 'output')
self.assertAllClose(
    expected_value.numpy(),
    results[signature_defs['serving_default']['outputs'][0]])

# Verify the SignatureDef structure returned is as expected.
self.assertEqual(len(signature_defs), 1)
self.assertEqual(list(signature_defs.keys()), ['serving_default'])
self.assertEqual(len(signature_defs.values()), 1)
self.assertEqual(
    list(signature_defs['serving_default'].keys()), ['inputs', 'outputs'])
self.assertCountEqual(signature_defs['serving_default']['inputs'], ['x'])
self.assertLen(list(signature_defs['serving_default']['outputs']), 1)
self.assertStartsWith(
    list(signature_defs['serving_default']['outputs'])[0], 'output')
