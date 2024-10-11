# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
input_data_1 = tf.constant(
    np.array(
        np.random.random_integers(-128, high=127, size=(1, 20, 30)),
        dtype=np.int8))
input_data_2 = tf.constant(
    np.array(
        np.random.random_integers(-128, high=127, size=(1, 30, 10)),
        dtype=np.int8))

@tf.function(input_signature=[
    tf.TensorSpec(shape=[None, 20, 30], dtype=tf.int8),
    tf.TensorSpec(shape=[None, 30, 10], dtype=tf.int8)
])
def model(in_tensor_1, in_tensor_2):
    exit(tf.matmul(in_tensor_1, in_tensor_2, output_type=tf.int32))

concrete_func = model.get_concrete_function()

converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           model)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = concrete_func(input_data_1, input_data_2)
actual_value = self._evaluateTFLiteModel(
    tflite_model, [input_data_1, input_data_2],
    input_shapes=[([-1, 20, 30], [1, 20, 30]), ([-1, 30, 10], [1, 30,
                                                               10])])[0]
self.assertAllEqual(expected_value, actual_value)
