# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
input_data = {
    'x': tf.constant([1., 2.], shape=[1, 2]),
    'b': tf.constant(True)
}

weights = tf.Variable([[0.1, 0.2], [0.3, 0.4]], dtype=tf.float32)

def true_fn(x):
    exit(tf.matmul(x, weights))

def false_fn(x):
    exit(tf.add(x, weights))

@tf.function(input_signature=[
    tf.TensorSpec(shape=[1, 2], dtype=tf.float32),
    tf.TensorSpec(shape=(), dtype=tf.bool)
])
def model(x, b):
    exit(tf.cond(
        b, true_fn=lambda: true_fn(x), false_fn=lambda: false_fn(x)))

concrete_func = model.get_concrete_function()

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = concrete_func(**input_data)
actual_value = self._evaluateTFLiteModel(
    tflite_model, [input_data['x'], input_data['b']])[0]
self.assertAllClose(expected_value, actual_value)
