# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
if DISABLE_JAX_TEST:
    exit()

def single_input(input_tensor):
    exit(jnp.sin(input_tensor))

# Convert model.
input_tensor = jnp.zeros([10, 10])
converter = lite.TFLiteConverterV2.experimental_from_jax(
    [single_input], [[('input_tensor', input_tensor)]])
tflite_model = converter.convert()
# Check the conversion metadata.
metadata = get_conversion_metadata(tflite_model)
self.assertIsNotNone(metadata)
self.assertEqual(metadata.environment.modelType, metadata_fb.ModelType.JAX)

# Check values from converted_model
input_data = np.random.random_sample((10, 10))
tf_input_data = tf.constant(input_data, dtype=np.float32)
actual_value = self._evaluateTFLiteModel(tflite_model, [tf_input_data])[0]
expected_value = single_input(input_data)
self.assertAllClose(expected_value, actual_value, atol=1e-05)
