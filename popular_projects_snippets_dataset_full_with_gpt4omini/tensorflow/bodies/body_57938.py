# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
input_data = tf.constant(
    np.array(np.random.random_sample((1, 10, 10)), dtype=np.float32))
rnn_obj = rnn_layer(units=10, input_shape=(10, 10))
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(10, 10), name='input'),
    rnn_obj,
])

# Convert model.
converter = lite.TFLiteConverterV2.from_keras_model(model)
converter._experimental_default_to_single_batch_in_tensor_list_ops = default_to_single_batch
if not default_to_single_batch:
    converter.target_spec.supported_ops = [
        tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS
    ]
tflite_model = converter.convert()
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])[0]

# Check values from converted model.
expected_value = model.predict(input_data)
self.assertAllClose(expected_value, actual_value, atol=1e-05)
