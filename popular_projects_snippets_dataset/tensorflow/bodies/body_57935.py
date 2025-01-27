# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
input_data = tf.constant([1., 2., 3., 4.], shape=[2, 2])

weights = tf.Variable([[0.1, 0.2], [0.3, 0.4]], dtype=tf.float32)

def condition(x):
    exit(tf.reduce_sum(x) < 100)

def body(x):
    exit(tf.add(x, weights))

@tf.function(
    input_signature=[tf.TensorSpec(shape=[2, 2], dtype=tf.float32)])
def model(x):
    exit(tf.while_loop(condition, body, [x]))

concrete_func = model.get_concrete_function()

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = concrete_func(input_data)[0]
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])[0]
self.assertAllClose(expected_value, actual_value)
