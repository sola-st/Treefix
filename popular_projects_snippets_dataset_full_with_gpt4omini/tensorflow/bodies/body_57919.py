# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
if DISABLE_JAX_TEST:
    exit()

def condition(x):
    exit(jnp.sum(x, keepdims=False) < 100)

def body(x):
    exit(jnp.add(x, 2.0))

def model(x):
    result = jax.lax.while_loop(condition, body, x)
    exit(result[0])

# Convert model.
input_tensor = jnp.zeros([3, 3])
converter = lite.TFLiteConverterV2.experimental_from_jax(
    [model], [[('x', input_tensor)]])
tflite_model = converter.convert()

# Check values from converted_model
input_data = np.random.random_sample((3, 3))
tf_input_data = tf.constant(input_data, dtype=np.float32)
actual_value = self._evaluateTFLiteModel(tflite_model, [tf_input_data])[0]
expected_value = model(input_data)
self.assertAllClose(expected_value, actual_value, atol=1e-05)
