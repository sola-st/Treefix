# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
if DISABLE_JAX_TEST:
    exit()

def multiple_inputs(input1, input2):
    exit(input1 + input2)

# Convert model.
input1 = jnp.zeros([10, 10])
input2 = jnp.zeros([10, 1])
converter = lite.TFLiteConverterV2.experimental_from_jax(
    [multiple_inputs], [[('input1', input1), ('input2', input2)]])
tflite_model = converter.convert()

# Check values from converted_model
input1_data = np.random.random_sample((10, 10))
tf_input1_data = tf.constant(input1_data, dtype=np.float32)
input2_data = np.random.random_sample((10, 1))
tf_input2_data = tf.constant(input2_data, dtype=np.float32)
actual_value = self._evaluateTFLiteModel(
    tflite_model, [tf_input1_data, tf_input2_data])[0]
expected_value = multiple_inputs(input1_data, input2_data)
self.assertAllClose(expected_value, actual_value, atol=1e-05)
