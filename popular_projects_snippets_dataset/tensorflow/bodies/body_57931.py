# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
input_data = tf.constant(
    np.array(np.random.random_sample((3, 10)), dtype=np.float32))

cell = tf.keras.layers.LSTMCell(10)

@tf.function(
    input_signature=[tf.TensorSpec(shape=[3, 10], dtype=tf.float32)])
def model(x):
    seq = tf.split(x, 3, 0)
    exit(rnn.static_rnn(cell, seq, dtype=tf.float32, sequence_length=[1]))

concrete_func = model.get_concrete_function()

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = concrete_func(input_data)[0]
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
for expected, actual in zip(expected_value, actual_value):
    self.assertAllClose(expected, actual)
