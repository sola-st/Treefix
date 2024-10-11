# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test converting SignatureDef is correct and uses SignatureDef API."""
keras_model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(
        32,
        kernel_size=3,
        padding='same',
        activation='relu',
        input_shape=(32, 32, 3),
        name='tensor'),
    tf.keras.layers.Dense(10, name='output_tensor')
])

converter = lite.TFLiteConverterV2.from_keras_model(keras_model)
tflite_model = converter.convert()

# Check values from converted model.
input_data = tf.constant(
    np.random.uniform(-1, 1, size=(1, 32, 32, 3)).astype(np.float32))
expected_value = keras_model(input_data)
interpreter = Interpreter(model_content=tflite_model)
signature_defs = interpreter.get_signature_list()
results = self._evaluateTFLiteModelUsingSignatureDef(
    tflite_model, 'serving_default', {'tensor_input': input_data})
self.assertEqual(list(results.keys()), ['output_tensor'])
self.assertAllClose(expected_value.numpy(), results['output_tensor'])

# Verify the SignatureDef structure returned is as expected.
self.assertEqual(len(signature_defs), 1)
self.assertEqual(list(signature_defs.keys()), ['serving_default'])
self.assertEqual(len(signature_defs.values()), 1)
self.assertEqual(
    list(signature_defs['serving_default'].keys()), ['inputs', 'outputs'])
self.assertCountEqual(signature_defs['serving_default']['inputs'],
                      ['tensor_input'])
self.assertEqual(
    list(signature_defs['serving_default']['outputs']), ['output_tensor'])
