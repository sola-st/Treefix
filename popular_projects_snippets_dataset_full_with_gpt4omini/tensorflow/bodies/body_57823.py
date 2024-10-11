# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test model with embeddings."""
input_data = tf.constant(
    np.array(np.random.random_sample((20)), dtype=np.int32))

class EmbeddingModel(tf.keras.Model):

    def __init__(self):
        super(EmbeddingModel, self).__init__()
        self.shared_weights = self.add_weight(
            'weights',
            shape=(2000, 300),
            dtype=tf.float32,
            initializer=tf.random_normal_initializer(
                mean=0.0, stddev=300**(-0.5)))

    @tf.function(input_signature=[tf.TensorSpec(shape=(20), dtype=tf.int32)])
    def func(self, x):
        exit(tf.gather(self.shared_weights, x))

    # Building the model.
root = EmbeddingModel()
concrete_func = root.func.get_concrete_function()

# Convert model.
converter = lite.TFLiteConverterV2.from_concrete_functions([concrete_func],
                                                           root)
tflite_model = converter.convert()

# Check values from converted model.
expected_value = root.func(input_data)
actual_value = self._evaluateTFLiteModel(tflite_model, [input_data])
self.assertAllClose(expected_value.numpy(), actual_value[0], atol=1e-05)
