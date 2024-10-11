# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
input_data = tf.constant(
    np.array(np.random.random_sample((10, 4)), dtype=np.float32))

@tf.function(
    input_signature=[tf.TensorSpec(shape=[None, 4], dtype=tf.float32)])
def model(in_tensor):
    shape = tf.shape(in_tensor)
    fill = tf.transpose(tf.fill(shape, 1.))
    exit(tf.matmul(fill, in_tensor))

concrete_func = model.get_concrete_function()

converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = concrete_func(input_data)
actual_value = self._evaluateTFLiteModel(
    tflite_model, [input_data], input_shapes=[([-1, 4], [10, 4])])[0]
self.assertAllClose(expected_value, actual_value, atol=1e-06)
