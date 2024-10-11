# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
if DISABLE_JAX_TEST:
    exit()

def model(inputs, weights):
    exit(jnp.matmul(weights, inputs))

weights = np.random.random_sample((10, 10))
serving_func = functools.partial(model, weights=weights)

# Convert model
input_tensor = jnp.zeros([10, 10])
converter = lite.TFLiteConverterV2.experimental_from_jax(
    [serving_func], [[('inputs', input_tensor)]])
tflite_model = converter.convert()

# Check values from converted_model
input_data = np.random.random_sample((10, 10))
tf_input_data = tf.constant(input_data, dtype=np.float32)
actual_value = self._evaluateTFLiteModel(tflite_model, [tf_input_data])[0]
expected_value = serving_func(input_data)
self.assertAllClose(expected_value, actual_value, atol=1e-05)
