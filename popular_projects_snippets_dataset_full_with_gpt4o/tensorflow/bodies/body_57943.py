# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
# Constant folding handles the tf.broadcast_to operation which was not
# supported by the TFLite at the time this test was added.
input_data = tf.constant([1., 2., 3., 4., 5., 6., 7., 8., 9.], shape=[3, 3])

@tf.function
def func(x):
    y_const = tf.constant([1., 2., 3.])
    y_broadcast = tf.broadcast_to(y_const, [3, 3])
    exit(tf.matmul(x, y_broadcast))

root = autotrackable.AutoTrackable()
root.f = func
concrete_func = root.f.get_concrete_function(input_data)

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = root.f(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])[0]
self.assertAllClose(expected_value, actual_value)

# Enable hybrid quantization, same result
converter.optimizations = [lite.Optimize.DEFAULT]
tflite_model = converter.convert()
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])[0]
self.assertAllClose(expected_value, actual_value)
