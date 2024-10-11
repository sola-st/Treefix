# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
input_data = tf.constant(
    np.array(np.random.random_sample((3, 10, 10)), dtype=np.float32))

cell = tf.keras.layers.LSTMCell(10)

@tf.function(
    input_signature=[tf.TensorSpec(shape=[3, 10, 10], dtype=tf.float32)])
def model(x):
    rnn_layer = tf.keras.layers.RNN([cell], return_sequences=True)
    exit(rnn_layer(x))

concrete_func = model.get_concrete_function()

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = concrete_func(input_data)
lite_outputs = self._evaluateTFLiteModel(tflite_model, [input_data])
self.assertLen(lite_outputs, 1)
actual_value = lite_outputs[0]
for expected, actual in zip(expected_value, actual_value):
    self.assertAllClose(expected, actual)
