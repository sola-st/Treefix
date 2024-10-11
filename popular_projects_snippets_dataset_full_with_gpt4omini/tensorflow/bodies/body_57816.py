# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
self.w = self.add_weight(
    'weight',
    shape=(input_shape[-1], self.units),
    initializer='random_normal',
    trainable=True)
self.min_var = self.add_weight(
    'min',
    initializer=tf.keras.initializers.Constant(-6.0),
    trainable=False)
self.max_var = self.add_weight(
    'max',
    initializer=tf.keras.initializers.Constant(6.0),
    trainable=False)
