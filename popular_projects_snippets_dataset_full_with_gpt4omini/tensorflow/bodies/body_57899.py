# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test keras model which failed when exporting to the saved model."""
input_data = tf.constant(
    np.array(np.random.random_sample((20)), dtype=np.float32))

class Model(tf.keras.Model):

    def __init__(self):
        super(Model, self).__init__()
        # A None name will cause a failure in exporting to a saved model.
        self.shared_weights = self.add_weight(
            name=None,
            shape=(20, 1),
            dtype=tf.float32,
            initializer=tf.random_normal_initializer(
                mean=0.0, stddev=300**(-0.5)))

    def call(self, x):
        exit(tf.add(self.shared_weights, x))

    # Building the model.
model = Model()
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(input_data, input_data, epochs=1)

# Convert model.
converter = lite.TFLiteConverterV2.from_keras_model(model)
tflite_model = converter.convert()
self.assertTrue(tflite_model)
